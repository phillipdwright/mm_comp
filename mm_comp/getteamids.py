"""get team data"""

import os
import re
import json

from mm_comp import getscoredata
from mm_comp.dates import (
    first_four_dates,
    first_round_dates
)

projectpath = os.path.dirname(__file__)

table_loader_dates = (
    first_four_dates +
    first_round_dates
)

teamdatafile = 'espnteamdata.json'

def main():
    espn_teams = {}
    team_attr = {'shortDisplayName', 'name', 'displayName'}
    scoredata = getscoredata(table_loader_dates)

    for event in scoredata:
        for competitor in event['competitions'][0]['competitors']:
            if int(competitor['id']) > 0: # id is -2 for teams still TBD
                team = competitor['team']
                # Grab the attributes we want
                teamdata = {k:v for k,v in team.items() if k in team_attr}
                # Add this team to the teams dictionary
                espn_teams.update({team['id']: teamdata})

    # Write ESPN team data to a file
    with open(os.path.join(projectpath, teamdatafile), 'w') as fn:
        json.dump(espn_teams, fn, indent=4)

    # Read team data from our database
    with open(os.path.join(projectpath, 'm_teams.json'), 'r') as fn:
        dbteams = json.load(fn)
    # Get ESPN team candidates for each of our teams
    for team in dbteams:
        candidates = getcandidates(team, espn_teams)
        team['candidates'] = candidates

    # Write team data back out to a file with ESPN candidates included
    with open(os.path.join(projectpath, 'm_teams.json'), 'w') as fn:
        json.dump(dbteams, fn, indent=4)


def getcandidates(dbteam, espnteams):
    # Looks through the espnteams dict and finds all candidates that could be
    #  a match for the dbteam dict that was passed in
    candidates = {}
    test_names = [dbteam['name']]
    test_names += dbteam['name'].replace('/', ' ').split()
    for id, team in espnteams.items():
        for name in test_names:
            pattern = re.compile(name)
            if re.search(
                pattern, 
                team['displayName'] + team['shortDisplayName']
            ):
                candidates[id] = team['displayName']
    return candidates


if __name__=='__main__':
    main()