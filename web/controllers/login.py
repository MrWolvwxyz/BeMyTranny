from flask import *
from hashlib import sha256
from extensions import mysql

fakeloggedin = True
fakeuserid = 12345

login = Blueprint('login', __name__, template_folder='templates')


@login.route('/login')
def loginfunc():
	error = None
	print ("hey I'm at the login page")
	return render_template('register.html',error=error)


@login.route('/register')
def registerfunc():
	error = None
	print ("hey I'm at the register page")
	return render_template('register.html',error=error)





