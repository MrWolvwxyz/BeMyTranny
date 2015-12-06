from flask import *
from hashlib import sha256

from extensions import mysql

fakeloggedin = True
fakeuserid = 12345

main = Blueprint('main', __name__, template_folder='templates')


@main.route('/')
@main.route('/index')
def index():
	cur=mysql.connection.cursor()
	cur.execute("select * from user")
	msgs=cur.fetchall()
	print msgs[0]

	if fakeloggedin:
		return render_template('userpage.html')
	return render_template('index.html',title='Home')






