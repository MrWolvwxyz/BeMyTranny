from app import app, db, models
from flask import render_template, redirect, url_for, request, session, flash
from hashlib import sha256

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           title='Home')

password_salt = "extrasalty"
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        user = request.form['username']
	pw_hash = sha256(password_salt+request.form['password']).hexdigest()
        query = models.User.query.filter_by(username=user)
	if query.count() == 0:
		error = 'Username not found'
		return render_template('login.html', error=error)
	query = query.filter_by(pw_hash=pw_hash)
	if query.count() == 0:
		error = 'Incorrect password'
		return render_template('login.html', error=error)
	#registered user
    	session['logged_in'] = True
    	print url_for('index')
    	return redirect(url_for('index'))
    return render_template('login.html', error=error)


@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        email = request.form['email']
        user = request.form['username']
	if models.User.query.filter_by(username=user).count() != 0:
		error = "Username already in use"
		return render_template('register.html', error=error)
	elif models.User.query.filter_by(email=email).count() != 0:
		error = "Email already in use"
		return render_template('register.html', error=error)
	pw_hash = sha256(password_salt+request.form['password']).hexdigest()
        u = models.User(username=user, pw_hash=pw_hash, email=email)
        db.session.add(u)
	db.session.commit()
    return render_template('register.html', error=error)

@app.route('/explorepage')
def explorepage():
    return render_template('explorepage.html')

@app.route('/logout')
def logout():
    error = None
    #session.pop('logged_in', None) #pops 'True' value off and replace with None
    return render_template('logout.html', error=error)

def return_home():  
    return redirect(url_for('Home')) #find a better redirect?

