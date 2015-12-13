from flask import *
from hashlib import sha256

from extensions import mysql

fakeloggedin = True
fakeuserid = 12345

about = Blueprint('about', __name__, template_folder='templates')


@about.route('/about', methods=['GET', 'POST'])
def aboutfunc():
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

	return render_template('about.html', **options)




