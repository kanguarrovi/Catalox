import os
import sqlite3
from flask import g

"""def return_engine():
	#return create_engine('sqlite:////home/kangu/Escritorio/restful-project/interview_question/database/salaries.db')
	return create_engine('sqlite:///' + os.getcwd() + '/vinyl-catalox.db')"""

DATABASE = os.getcwd() + '/catalox.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

"""@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()"""

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv