# foosball_scores
To install:

`vagrant up`
`vagrant ssh`
`cd /vagrant/foosball_scores`
`sudo apt-get install python-pip`
`sudo pip install -r requirements.txt`
`python manage.py runserver 0.0.0.0:8000`

You should then be able to go to `localhost:8000/admin` on your browser and access the site.
Login and password are both `admin`