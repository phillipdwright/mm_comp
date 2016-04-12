from urllib.request import urlopen
import json
from bs4 import BeautifulSoup

bb_urlbase = 'http://espn.go.com/mens-college-basketball/scoreboard/_/date/'
missing_scoreboard = 'ERROR: No scoreboard found for {}!'
malformed_scoreboard = 'ERROR: Scoreboard data for {} does not match pattern!'
# Start and end anchors for json scoreboard data string in script on ESPN page
jstringstart = '{'
jstringend = ';window.espn.scoreboardSettings ='

def getscoredata(dates, urlbase=bb_urlbase):
    # Takes a list of dates formatted YYYYMMDD and an optional url base for
    # the ESPN scoreboard site. Returns a list of events.
    scoredata = []
    # Build  dict pulling data from each day in tourney
    for date in dates:
        url = urlbase + date
        page = urlopen(url)
        soup = BeautifulSoup(page.read(), 'html.parser')
        scoreboard = ''
        for script in soup.find_all('script'):
            if script.get_text().startswith('window.espn.scoreboardData'):
                scoreboard = script.get_text()
        # Print an error & skip to the next date if there is no scoreboard
        if not scoreboard:
            print(missing_scoreboard.format(date))
            continue
        # Print an error & skip to the next date if the scoreboard is malformed
        try:
            jstart = scoreboard.index(jstringstart)
            jend = scoreboard.index(jstringend)
        except:
            print(malformed_scoreboard.format(date))
            continue
        # Parse json and store each event from it into scoredata
        events = json.loads(scoreboard[jstart:jend])['events']
        for event in events:
            scoredata.append(event)

    return scoredata