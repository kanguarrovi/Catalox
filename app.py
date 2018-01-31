import sqlite3 as sql
from flask import Flask, render_template
from database.connection import query_db

app = Flask(__name__, static_url_path='/static')

@app.route('/')
@app.route('/index')
def index():
	con = sql.connect("database/vinyl-catalox.db")
	con.row_factory = sql.Row
	cur = con.cursor()
	cur.execute("select * from Vinyl")
	albums = cur.fetchall()
	if len(albums) > 0:
		return render_template('index.html', albums=albums)
	else:
		msg = 'No Articles found'
		return render_template('index.html', msg=msg)

if __name__ == '__main__':
	app.run(debug=True)