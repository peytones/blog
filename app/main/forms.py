from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import Required, Email, Length

class NameForm(Form):
	name = StringField('What is your name?', validators=[Required()])
	submit = SubmitField('Submit')

class LoginForm(Form):
	email = StringField('Email', validators=[Required(), Length(1, 64), Email()])
	password = PasswordField('Password', validators=[Required()])
	remembder_me = BooleanField('Keep me logged in')
	submit = SubmitField('Log In')