from app import app, db
from flask import render_template, redirect, url_for, request, session, flash

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html',
                           title='Home')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin':
            error = 'Invalid credentials'
        else:
            session['logged_in'] = True
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    error = None
    #session.pop('logged_in', None) #pops 'True' value off and replace with None
    return render_template('logout.html', error=error)

def return_home():  
    return redirect(url_for('home')) #find a better redirect?

