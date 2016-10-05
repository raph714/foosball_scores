# Foosball Scores (or any other sport that involves random teams really)

Track a leaderboard of players based on games played with varying random teams. The algorithm takes the aggregated scores of the winning and losing teams to distribute points based on the point total of the game. The higher the point differential, the higher the stakes for the team with more points at the start of a match.

Each player is initially awarded 1000 points, and moves up and down based on wins and losses from there.


### To install:

`vagrant up`

`vagrant ssh`

`cd /vagrant/foosball_scores`

`sudo apt-get install python-pip`

`sudo pip install -r requirements.txt`

`python manage.py runserver 0.0.0.0:8000`

You should then be able to go to `localhost:8000/admin` on your browser and access the site.
Login and password are both `admin`
