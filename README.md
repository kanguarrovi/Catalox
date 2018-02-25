# Catalox 

A simple vinyl catalog developed in Python/Flask.

### What is this repository for? ###

* Quick summary
* Version: 1.0

## Installation 

Clone this repository 

	$ git clone https://github.com/kanguarrovi/catalox.git

Create a virtualenv (on Debian based Linux)

    $ cd catalox
	$ python3 -m venv catalox
	$ source catalox/bin/activate

Create a virtualenv (on Windows)

    $ C:\Users\Name>cd catalox
	$ C:\Users\Name\catalox> C:\Python35\python -m venv catalox
	$ C:\Users\Name\catalox> catalox\Scripts\activate

Upgrade pip if it is needed 

	$ pip install --upgrade pip

Install requirements 

	$ pip install -r requirements.txt

Start Database

	$ export FLASK_APP=catalox.py
	$ flask db init
    $ flask db migrate -m "Initial migration"
    $ flask db upgrade

## Run in development

	$ export FLASK_APP=catalox.py
	$ flask run

    Go to the browser at 127.0.0.1:5000 and begin to use it.


