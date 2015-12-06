from flask import *
from hashlib import sha256

from extensions import mysql

fakeloggedin = False
fakeuserid = 12345

userpage = Blueprint('userpage', __name__, template_folder='templates')


@userpage.route('/userpage')
def userpagefunc():
	error = None
	return render_template('userpage.html', error = error)







