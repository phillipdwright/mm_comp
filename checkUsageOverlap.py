#!/usr/bin/python

import MySQLdb

# connect to the database
db = MySQLdb.connect(host="",
                     user="",
                     passwd="",
                     db="")

# create a Cursor object -- it will let us execute queries
cur = db.cursor()

# grab some data
cur.execute("SELECT id, displayname FROM m_entries WHERE mid = 1")

# store names in a list, and IDs in another
names = []
name_IDs = []
name_choices = []

for row in cur.fetchall():
    names.append(row[1])
    name_IDs.append(row[0])
    name_choices.append([])

print names
print name_IDs

# open files for writing
"""Commented out by Phil"""
# f1 = open('overlap.csv','w')
# f2 = open('usage.csv','w')

# for each person, make a list of that person's choices
for i in range(len(name_IDs)):
    cur_list = []
    cur.execute("SELECT tid FROM m_entries_data WHERE mid = 1 AND eid = %s", name_IDs[i])
    for row in cur.fetchall():
        cur_list.append(row[0])
    name_choices[i] = cur_list

# iterate through all people, and compare versus everyone else (bidirectional is cool)
"""File open statement added by Phil"""
with open('overlap.csv','w') as f1:
    for i in range(len(name_IDs)):
        for j in range(i+1,len(name_IDs)):
            tmp = set(name_choices[i]).intersection(name_choices[j])
            # print(names[i] + " and " + names[j] + " overlap in " + str(len(tmp)) + " teams: " + str(tmp))
            f1.write(str(len(tmp)) + "," + names[i] + "," + names[j] + "," + str(tmp) + "\n")

# let's get usage data on each of the 64 teams!
cur.execute("SELECT id, name FROM m_teams WHERE mid = 1 ORDER BY seed ASC, lid ASC")

total = len(name_IDs)
ftotal = float(total)

"""File open statement added by Phil"""
with open('usage.csv', 'w') as f2:
    for row in cur.fetchall():
        tid = row[0]
        ctotal = 0
        tname = row[1]
        for i in range(total):
            if tid in name_choices[i]:
                ctotal = ctotal + 1
        # print(tname + " is in " + str(ctotal) + " of entries (" + str(100*ctotal/ftotal) + "%).")
        f2.write(tname + "," + str(ctotal) + "," + str(100*ctotal/ftotal) + "\n")

print("Total number of entries is: " + str(total))
"""Commented out by Phil"""
# f1.close()
# f2.close()
db.close()
