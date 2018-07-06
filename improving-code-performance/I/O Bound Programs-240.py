## 2. Profiling an I/O bound task ##

import cProfile
import sqlite3

query = "SELECT DISTINCT teamID from Teams inner join TeamsFranchises on Teams.franchID == TeamsFranchises.franchID where TeamsFranchises.active = 'Y';"
conn = sqlite3.connect("lahman2015.sqlite")

cur = conn.cursor()
teams = [row[0] for row in cur.execute(query).fetchall()]
query = "SELECT SUM(HR) FROM Batting WHERE teamId=?"
def calculate_runs(teams):
    home_runs = []
    for team in teams:
        runs = cur.execute(query, [team]).fetchall()
        runs = runs[0][0]
        home_runs.append(runs)
    return home_runs

profile_string = "home_runs = calculate_runs(teams)"
cProfile.run(profile_string)

## 3. Blocking Tasks ##

import sqlite3

memory = sqlite3.connect(':memory:') # create a memory database
disk = sqlite3.connect('lahman2015.sqlite')

dump = "".join([line for line in disk.iterdump() if "Batting" in line])
memory.executescript(dump)

cur = memory.cursor()
query = "SELECT SUM(HR) FROM Batting WHERE teamId=?"
def calculate_runs(teams):
    home_runs = []
    for team in teams:
        runs = cur.execute(query, [team]).fetchall()
        runs = runs[0][0]
        home_runs.append(runs)
    return home_runs

profile_string = "home_runs = calculate_runs(teams)"
cProfile.run(profile_string)