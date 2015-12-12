from flask import *
from hashlib import sha256

from extensions import mysql

fakeloggedin = True
fakeuserid = 12345

explorepage = Blueprint('explorepage', __name__, template_folder='templates')


@explorepage.route('/explorepage', methods=['GET', 'POST'])
def explorepagefunc():
	options=\
	{
		"login": False,
		"username": "",
		"status": 0
	}

	if request.method == 'GET':
		cur=mysql.connection.cursor()
		cur.execute("select * from post")
		msgs = [];
		msgs=cur.fetchall()
		if session.has_key('username'):
			options["login"]=True
			options["username"]=session["username"]
		print ("this is a get method") 
	return render_template('explorepage.html', data = msgs, **options )




