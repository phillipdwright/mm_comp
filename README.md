# mm_comp
A collection of scripts for database setup and back-end maintenance for Roanoke College's March Madness competition, using score data scraped from ESPN's scoreboard website

## Installation
This will install the **mm_comp** project to your default install location for third-party modules.

To install, run:
```
git clone https://github.com/phillipdwright/mm_comp.git
python setup.py
```

To uninstall, run:
```
pip uninstall mm_comp
```

## Getting Started
First, create the database required for the competition, run ``bowl.sql``.
Next, set up ``db_connector.py`` and ``update_email.py`` in your project root 
directory.  ``db_connector.py`` should contain a dictionary of parameters to connect to the 
database you created.  ``update_email.py`` should contain a url called ``points_update`` that 
will call an update script and a function called ``email_report`` that takes an email string
as a parameter and sends an email containing this email string as the body.

## Usage
Once the back-end database is created and ESPN has published information for the tournament, 
change ``dates.py`` to show the tournament dates for each round.
* ``getteamids.py`` will obtain data on all teams in the tournament from espn.com.  This is a setup task
and will only need to be run once.
* ``addespnids.py`` writes the teams ids from espn.com to the competition website.  This is a setup task
and will only need to be run once.
* ``update_wins.py`` checks ESPN's scoreboard and updates the database with current score information,
if any games have completed since the last update.  This should be scheduled to run periodically (eg., every 30
minutes) throughout the tournament to update the competition website regularly.
* ``update_possible.py`` is called by ``update_wins.py`` if any games have completed since the last update.  This
script updates the database with accurate figures for the maximum number of points a competitor may be able to
obtain through the remainder of the tournament.

## Compatibility
This project was developed using Python 3.4 and is compatible with versions 3.4 and 3.5.

## Credits
* **[Phil Wright](https://github.com/phillipdwright)**: Developed the update code to manage the competition using ESPN
* **[David Taylor](https://github.com/uvadavey79)**: Developed the database and the website to run the competition
