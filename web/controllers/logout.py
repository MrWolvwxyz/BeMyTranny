from flask import *
from hashlib import sha256

from extensions import mysql



logout = Blueprint('logout', __name__, template_folder='templates')


@logout.route('/logout',  methods=['GET', 'POST'])
def logoutfunc():
	error = None
	if request.method=='POST':
		session.pop('logged_in', None)
		print ('You have logged out')
		return render_template('index.html', error = error)

	return render_template('logout.html', error = error)




