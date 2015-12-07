from flask import *
from hashlib import sha256

from extensions import mysql

fakeloggedin = False
fakeuserid = 12345

addmoreresponse = Blueprint('addmoreresponse', __name__, template_folder='templates')


@addmoreresponse.route('/addmoreresponse')
def addmoreresponsefunc():
	error = None
	return render_template('addmoreresponse.html', error = error)







