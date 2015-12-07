from flask import *
from hashlib import sha256
from extensions import mysql

fakeloggedin = True
fakeuserid = 12345

login = Blueprint('login', __name__, template_folder='templates')


@login.route('/login', methods = ['GET', 'POST'])
def loginfunc():
	error = None
	if request.method == 'POST' and request.form['operation'] == 'login':
		print ("hey I'm at the login page")
		cur = mysql.connection.cursor()
		cur.execute("select password from user where username = '" + request.form['username'] + "';")
		password = cur.fetchall()
		if password:
			print(request.form['password'], password[0][0])
			if password[0][0] == request.form['password']:
				print('found username password pair')
				session['username'] = request.form['username']
				return render_template('register.html', error = error)
			else:
				error = 'you entered the wrong password for this username'
				print('wrong password for username')
				return render_template('register.html', error = error)
		else:
			error = 'username not found'
			print('username not found')
			return render_template('register.html', error = error)
	elif request.method == 'POST' and request.form['operation'] == 'register':
		print ("hey I'm at the register page")
		cur = mysql.connection.cursor()
		username = request.form['username']
		password = request.form['password']
		email = request.form['email']
		print("insert into user (username,password,email) values ('" + username + "', '" + password + "', '" + email + "';")
		cur.execute("insert into user (username,password,email) values ('" + username + "', '" + password + "', '" + email + "');")
		cur.execute("commit")
		session['username'] = request.form['username']
		print('exiting post logic')
	return render_template('register.html',error=error)





