from flask_wtf import FlaskForm
#from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms import Form, BooleanField, StringField, IntegerField, FloatField, SelectField, PasswordField, validators
from wtforms.validators import DataRequired

"""class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')"""

class AlbumForm(Form):
	#Image to consider
	artist = StringField('Artist', [validators.Length(min=1)])
	name = StringField('Album', [validators.Length(min=1)])
	price = FloatField('Price',[validators.NumberRange(min=0)])
	status = SelectField('Status', choices=[('ava', 'Available'), ('sav', 'Saved'), ('sld', 'Sold')])
	info = StringField('Info')