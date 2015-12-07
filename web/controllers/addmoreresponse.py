from flask import *
from hashlib import sha256

from extensions import mysql

fakeloggedin = False
fakeuserid = 12345

addmoreresponse = Blueprint('addmoreresponse', __name__, template_folder='templates')


@addmoreresponse.route('/addmoreresponse')
def addmoreresponsefunc():
	options=\
	{
		"login": False,
		"username": "",
		"status": 0
	}
	error = None
	if session.has_key('username'):
		options["login"]=True
		options["username"]=session["username"]
	if request.method == 'GET':
		print ("this is get")
		
	return render_template('addmoreresponse.html', error = error, **options)







