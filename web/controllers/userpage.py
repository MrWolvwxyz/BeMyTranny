from flask import *
from hashlib import sha256

from extensions import mysql

fakeloggedin = False
fakeuserid = 12345

userpage = Blueprint('userpage', __name__, template_folder='templates')


@userpage.route('/userpage')
def userpagefunc():
	error = None
	if not session.has_key('username'):
		return render_template('errorpage.html', error = error)

	if request.method == 'GET':
		name = session['username']
		print ("this is a get method") 
	return render_template('userpage.html', error = error, name = name)







