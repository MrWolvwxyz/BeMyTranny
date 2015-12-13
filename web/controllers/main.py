from flask import *
from hashlib import sha256

from extensions import mysql



main = Blueprint('main', __name__, template_folder='templates')


@main.route('/')
@main.route('/index')
def index():

	cur=mysql.connection.cursor()
	cur.execute("select * from user")
	msgs = [];
	msgs=cur.fetchall()
	print msgs
	#print msgs[0][1]
	if session.has_key("username"):
		return redirect('/userpage')
	return render_template('index.html',title='Home')






