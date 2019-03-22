from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length

app = Flask(__name__)
app.config['SECRET_KEY'] = 'This is SeCret!'
Bootstrap(app)

class LoginForm(FlaskForm):
	username = StringField('username', validators=[InputRequired(), Length(min=4, max=20)])
	password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
	remember = BooleanField('remember me')

class RegisterForm(FlaskForm):
	email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
	username = StringField('username', validators=[InputRequired(), Length(min=4, max=20)])
	password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])

@app.route("/")
@app.route("/Home")
def home():
	return render_template('home.html')

@app.route("/About")
def about():
	return render_template('about.html', title='About')

@app.route("/Login", methods=['GET', 'POST'])
def login():
	form = LoginForm()
	return render_template('login.html', title='Login', form=form)

@app.route("/Signup", methods=['GET', 'POST'])
def signup():
	form = RegisterForm()
	return render_template('signup.html', title='Sign Up', form=form)

@app.route("/Apex")
def apex():
	return render_template('apex.html', title='Apex Legends')

@app.route("/Rocket League")
def rl():
	return render_template('rl.html', title='Rocket League')

@app.route("/CounterStrike GlobalOffensive")
def csgo():
	return render_template('csgo.html', title='CS:GO')

@app.route("/Black Ops 4")
def bo4():
	return render_template('bo4.html', title='Black Ops 4')

@app.route("/Mortal Kombat X")
def mkx():
	return render_template('mkx.html', title='Mortal Kombat X')

@app.route("/Overwatch")
def overwatch():
	return render_template('overwatch.html', title='Overwatch')

@app.route("/Grand Theft Auto 5")
def gta5():
	return render_template('gta5.html', title='Grand Theft Auto 5')

@app.route("/PUBG")
def pubg():
	return render_template('pubg.html', title='PUBG')
