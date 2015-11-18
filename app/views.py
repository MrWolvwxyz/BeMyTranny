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
            return redirect(url_for('index'))
        else:
            error = 'Are you sure you registered?' 
        #u = models.User(username=user, email=email)
        #db.session.add(u)
        #db.session.commit()
    return render_template('login.html', error=error)


@app.route('/register', methods=['GET', 'POST'])
def register():
    error = 'All good'
    email = request.form['email']
    user = request.form['username']
    u = models.User(username=user, email=email)
    db.session.add(u)
    return render_template('register.html', error=error)



@app.route('/logout')
def logout():
    error = None
    #session.pop('logged_in', None) #pops 'True' value off and replace with None
    return render_template('logout.html', error=error)

def return_home():  
    return redirect(url_for('Home')) #find a better redirect?

