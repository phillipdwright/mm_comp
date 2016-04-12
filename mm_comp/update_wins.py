"""Update wins on MM website db using espn data"""

from urllib.request import urlopen
import json
from bs4 import BeautifulSoup
import pymysql.cursors
import os

projectpath = os.path.dirname(__file__)

from mm_comp import getscoredata
# Import the parameters for the database connection
from mm_comp.db_connector import connection_params
# Import the function to email a report and the url to run a the points update
# script
from mm_comp.update_email import email_report, points_update
from mm_comp import update_possible
from mm_comp.dates import (
    first_round_dates,
    second_round_dates,
    sweet_sixteen_dates,
    elite_eight_dates,
    final_four_dates,
    championship_dates
)

tourney_dates = (
    first_round_dates +
    second_round_dates +
    sweet_sixteen_dates +
    elite_eight_dates +
    final_four_dates +
    championship_dates
)


def main():
    needs_updating = False

    # Get html page, find json data within it, process it, and put each event
    # dict into a scoredata list
    scoredata = getscoredata(tourney_dates)
    email_string = ''

    # Connect to the database
    db = pymysql.connect(**connection_params)

    # Get m_games, and store gameids from it in gameids
    selectquery = 'SELECT gameid FROM m_games WHERE mid=1'
    cur = db.cursor()
    cur.execute(selectquery)
    gameids = []
    for row in cur.fetchall():
        gameids.append(row[0])

    # Cycle through events in scoredata, check to see if they're completed,
    # and check to see if they're in our site db. If not, add their results.
    insertstatement = 'INSERT INTO m_games (gameid, winner, loser, mid) VALUES'
    insertstatement += ' (%s, %s, %s, 1)'
    for event in scoredata:
        completed = event['competitions'][0]['status']['type']['completed']
        eventid = event['id']
        if completed:
            if int(eventid) not in gameids:
                email_string += 'Updating event ' + eventid + '\n'
                for competitor in event['competitions'][0]['competitors']:
                    if competitor['winner']:
                        winner = competitor['id']
                    else:
                        loser = competitor['id']
                data = (eventid, winner, loser)
                cur.execute(insertstatement, data)
                needs_updating = True
            else:
                email_string += 'Event ' + eventid + ' not updated.\n'
    cur.close()
    db.commit()

    # If any changes have been made to m_games, update m_teams and run the
    # points update php script.
    selectteamsquery = 'SELECT id, espnid FROM m_teams WHERE mid=1'
    selectwinnerquery = 'SELECT winner FROM m_games WHERE mid=1 '
    selectwinnerquery += 'AND winner = %s'
    selectloserquery = 'SELECT loser FROM m_games WHERE mid=1 AND loser = %s'
    updateteamquery = 'UPDATE m_teams SET wins=%s, inactive=%s '
    updateteamquery += 'WHERE mid=1 AND id=%s'
    if needs_updating:
        email_string += 'We are updating m_teams.\n'
        cur = db.cursor()
        cur.execute(selectteamsquery)

        for team in cur.fetchall():
            espnid = team[1]
            # Is there a mysqldb function that gives us the number of rows
            # without returning data?
            cur.execute(selectwinnerquery, (espnid))
            wins = cur.rowcount
            cur.execute(selectloserquery, (espnid))
            inactive = cur.rowcount
            data = (wins, inactive, team[0])
            cur.execute(updateteamquery, data)

        cur.close()
        db.commit()
        urlopen(points_update)
        update_possible.main()

        # Send email if something was updated!
        email_report(email_string)

    db.close()


if __name__ == '__main__':
    main()
