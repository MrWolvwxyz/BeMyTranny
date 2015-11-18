from app import app, db, models
from flask import render_template, redirect, url_for, request, session, flash

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           title='Home')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        user = request.form['username']
        query = models.User.query.filter_by(username=user).first()
        if query is not None: #registered user
            session['logged_in'] = True
            print url_for('index')
            return redirect(url_for('index'))
        else:
            error = 'Are you sure you registered?' 
    return render_template('login.html', error=error)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        error = None
        print('error here')
        email = request.form['email']
        print('error there')
        user = request.form['username']
        print('error')
        u = models.User(username=user, email=email)
        print('now here')
        db.session.add(u)
    return render_template('register.html')# , error=error)

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

