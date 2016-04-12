"""Update points possible after each game"""

import pymysql.cursors
from mm_comp.db_connector import connection_params


# Select id and points from entries table
selectentriesquery = 'SELECT id, points FROM m_entries WHERE mid=1'
selectteamsquery = 'SELECT t.id, t.lid, t.seed, t.wins, t.inactive FROM '
selectteamsquery += 'm_teams as t, m_entries_data as e WHERE t.mid=1 AND '
selectteamsquery += 't.id=e.tid AND t.inactive=0 AND e.eid=%s'
selecteventsquery = 'SELECT round FROM m_events WHERE id=1'
updatequery = 'UPDATE m_entries SET possible=%s WHERE id=%s'

seeds = [
    [
        [
            [1, 16],
            [8, 9]
        ],
        [
            [5, 12],
            [4, 13]]
    ],
    [
        [
            [6, 11],
            [3, 14]
        ],
        [
            [7, 10],
            [2, 15]
        ]
    ]
]

def flatten(list_of_lists):
    flat_list = list_of_lists
    while isinstance(flat_list[0], list):
        flat_list = [val for sublist in flat_list for val in sublist]
    return flat_list


oneset = set(flatten(seeds[0][0]))
twoset = set(flatten(seeds[0][1]))
redset = set(flatten(seeds[1][0]))
blueset = set(flatten(seeds[1][1]))


def main():
    # Open db connection and create cursor
    db = pymysql.connect(**connection_params)
    cur = db.cursor()

    # Get round from m_events
    cur.execute(selecteventsquery)
    round = cur.fetchone()[0]

    # Iterate through each entry in the competition
    cur.execute(selectentriesquery)
    for entry in cur.fetchall():
        id = entry[0]
        pointspossible = entry[1] # Initialize as the current points tally
        cur.execute(selectteamsquery, (id))
        teams = cur.fetchall()

        # Check to see if anyone is left to win the championship
        if round < 6:
            if teams:
                pointspossible += 12

        # Check to see if anyone is left to win each final four match
        if round < 5:
            for team in teams:
                wins = team[3]
                if wins < 5: # Only count if they haven't already won this round
                    if team[1] in (1, 3):
                        pointspossible += 9
                        break
            for team in teams:
                wins = team[3]
                if wins < 5: # Only count if they haven't already won this round
                    if team[1] in (2, 4):
                        pointspossible += 9
                        break

        # Check to see if anyone is left to win each elite eight match
        if round < 4:
            locations = set()
            for team in teams:
                wins = team[3]
                if wins < 4: # Only count if they haven't already won this round
                    locations.add(team[1])
            pointspossible += 7 * len(locations)

        # Check to see if anyone is left to win each sweet sixteen match
        if round < 3:
            regions = {}
            topset = set(flatten(seeds[0]))
            bottomset = set(flatten(seeds[1]))
            for region in range(1, 5):
                regions[region] = set()
            for team in teams:
                # Add the seed value to the set for that team's region
                wins = team[3]
                if wins < 3: # Only count if they haven't already won this round
                    regions[int(team[1])].add(team[2])
            for region in range(1, 5):
                if topset.intersection(regions[region]):
                    pointspossible += 5
                if bottomset.intersection(regions[region]):
                    pointspossible += 5

        # Store the calculated points possible value for this entry
        data = (str(pointspossible), id)
        cur.execute(updatequery, data)

    cur.close()
    db.commit()
    db.close()


if __name__ == '__main__':
    main()