"""Update m_teams table with espn ids."""

import json
import pymysql.cursors
import os

from mm_comp.db_connector import connection_params

projectpath = os.path.dirname(__file__)

db = pymysql.connect(**connection_params)

with open(os.path.join(projectpath, 'm_teams_updated.json'), 'r') as fn:
    teamdata = json.load(fn)

selectquery = 'SELECT id FROM m_teams WHERE mid=1'
updatequery = 'UPDATE m_teams SET espnid = %s WHERE id=%s'

# create a Cursor object -- it will let us execute queries

cur = db.cursor()

cur.execute(selectquery)
for row in cur.fetchall():
    id = row[0]
    espnid = ''
    for team in teamdata:
        if team['id'] == str(id):
            for k in team['candidates']:
                espnid = k
            break
    print('id = ' + str(id) + ', & espnid = ' + espnid)
    cur.execute(updatequery, (espnid, str(id)))
    
cur.close()
db.commit()
db.close()