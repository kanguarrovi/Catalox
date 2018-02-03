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
	con.close()
	if len(albums) > 0:
		return render_template('index.html', albums=albums)
	else:
		msg = 'No Articles found'
		return render_template('index.html', msg=msg)

@app.route('/album/<string:id>')
def album(id):
	con = sql.connect("database/vinyl-catalox.db")
	con.row_factory = sql.Row
	cur = con.cursor()
	cur.execute("SELECT * FROM Vinyl WHERE id =" + id)
	album = cur.fetchone()
	con.close()
	return render_template('album.html', album=album)

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
		con.close()
		return redirect(url_for('dashboard'))
	return render_template('album_form.html', action="Add", form = form)

@app.route('/dashboard')
def dashboard():
	con = sql.connect("database/vinyl-catalox.db")
	con.row_factory = sql.Row
	cur = con.cursor()
	cur.execute("SELECT * FROM Vinyl")
	albums = cur.fetchall()
	con.close()
	if len(albums) > 0:
		return render_template('dashboard.html', albums = albums)
	else:
		msg = 'No Articles found'
		return render_template('dashboard.html', msg = msg)

@app.route('/edit_album/<string:id>', methods=['GET', 'POST'])
def edit_article(id):

	con = sql.connect("database/vinyl-catalox.db")
	con.row_factory = sql.Row
	cur = con.cursor()
	cur.execute("SELECT * FROM Vinyl WHERE id =" + id)

	album = cur.fetchone()
	con.close()

	#Get form
	form = AlbumForm(request.form)

	#Populate article form fields

	form.artist.data = album['artist']
	form.name.data = album['name']
	form.price.data = album['price']
	form.saved.data = album['saved']
	form.sold.data = album['sold']
	form.info.data = album['info']

	if request.method == 'POST' and form.validate():

		print("This is the form", request.form)

		artist = request.form['artist']
		name = request.form['name']
		price = request.form['price']

		saved = 0 if request.form['saved'] == None else 1
		sold = 0 if request.form['sold'] == None else 1

		info = request.form['info']

		con = sql.connect("database/vinyl-catalox.db")
		cur = con.cursor()

		#Execute
		cur.execute("UPDATE Vinyl SET artist='"+ artist
			+"', name='" + name 
			+ "', price='" + str(price) 
			+ "', saved='" + str(saved)
			+ "', sold='" + str(sold) 
			+ "', info='" + info +"' WHERE id=" + id)

		#Commit to DB
		con.commit()
		con.close()

		return redirect(url_for('dashboard'))

	return render_template('album_form.html', action="Edit", form = form)


@app.route('/delete_album/<string:id>', methods=['POST'])
def delete_album(id):
	con = sql.connect("database/vinyl-catalox.db")
	cur = con.cursor()
	cur.execute("DELETE FROM vinyl WHERE id=" + id)
	con.commit()
	cur.close()
	return redirect(url_for('dashboard'))

if __name__ == '__main__':
	app.secret_key = 'thereisnothingtodo'
	app.run(debug=True)