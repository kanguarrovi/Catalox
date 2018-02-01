import sqlite3 as sql
from flask import Flask, render_template, flash, redirect, url_for, request
from database.connection import query_db
from wtforms import Form, BooleanField, StringField, IntegerField, PasswordField, validators

app = Flask(__name__, static_url_path='/static')

#Main page
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

#Album form
class AlbumForm(Form):
	#Image to consider
	artist = StringField('Artist', [validators.Length(min=1)])
	name = StringField('Album', [validators.Length(min=1)])
	price = IntegerField('Price',[validators.NumberRange(min=0)])
	saved = BooleanField('Saved')
	sold = BooleanField('Sold')
	info = StringField('Info')

@app.route('/add_album', methods=['GET', 'POST'])
def add_album():
	form = AlbumForm(request.form)
	if request.method == 'POST' and form.validate():
		artist = form.artist.data
		name = form.name.data
		price = form.price.data
		saved = 1 if form.saved.data else 0
		sold = 1 if form.sold.data else 0
		info = form.info.data

		con = sql.connect("database/vinyl-catalox.db")
		cur = con.cursor()
		cur.execute("INSERT INTO Vinyl(artist, name, price, saved, sold, info) VALUES('"
			+ artist +"','"
			+ name + "',"
			+ str(price) + ","
			+ str(saved) + ","
			+ str(sold) + ","
			+ "'" + info + "')"
		)
		con.commit()
		return redirect(url_for('index'))
	return render_template('add_album.html', form = form)

if __name__ == '__main__':
	app.secret_key = 'thereisnothingtodo'
	app.run(debug=True)