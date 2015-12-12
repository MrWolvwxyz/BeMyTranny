from flask import *
from hashlib import sha256

from extensions import mysql



logout = Blueprint('logout', __name__, template_folder='templates')


@logout.route('/logout',  methods=['GET', 'POST'])
def logoutfunc():
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
	if request.method=='POST':
		session.pop('logged_in', None)
		session.clear()
		print ('You have logged out')
		return redirect('/index')

	return render_template('logout.html', error = error, **options)




