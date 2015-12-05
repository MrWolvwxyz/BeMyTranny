from app import app, db, models
from flask import render_template, redirect, url_for, request, session, flash
from hashlib import sha256


fakeloggedin = True
fakeuserid = 12345

@app.route('/')
@app.route('/index')
def index():
    if fakeloggedin:
        return render_template('userpage.html')
    return render_template('index.html',title='Home')

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
		return render_template('register.html', error=error)
	query = query.filter_by(pw_hash=pw_hash)
	if query.count() == 0:
		error = 'Incorrect password'
		return render_template('register.html', error=error)
	#registered user
    	session['logged_in'] = True
    	print url_for('index')
    	return redirect(url_for('index'))
    return render_template('register.html', error=error)


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
    if request.method == 'GET':

        class fakePost:

            def __init__(self, uid, tit, des, ori, tar, path):
                self.userid = uid;
                self.title = tit;
                self.description = des;
                self.origin = ori;
                self.target = tar;
                self.pathofIMG = path;

        myfakePost = []

        myfakePost.append(fakePost(1,"post1","description for post1","Chinese","English","kshirt.jpg"))
        myfakePost.append(fakePost(2,"post2","description for post2","Chinese","English","kshirt.jpg"))
        myfakePost.append(fakePost(3,"post3","description for post3","Chinese","English","kshirt.jpg"))
        myfakePost.append(fakePost(4,"post4","description for post4","Chinese","English","kshirt.jpg"))
        myfakePost.append(fakePost(5,"post5","description for post5","Chinese","English","kshirt.jpg"))
        myfakePost.append(fakePost(6,"post6","description for post6","Chinese","English","kshirt.jpg"))
        myfakePost.append(fakePost(7,"post7","description for post7","Chinese","English","kshirt.jpg"))

        print ("this is a get method") 
    return render_template('explorepage.html', data = myfakePost)

@app.route('/logout')
def logout():
    error = None
    #session.pop('logged_in', None) #pops 'True' value off and replace with None
    return render_template('logout.html',  error=error)


@app.route('/home')
def home():
    error = None
    #session.pop('logged_in', None) #pops 'True' value off and replace with None
    return render_template('userpage.html',  error=error)



@app.route('/ask')
def ask():
    error = None
    #session.pop('logged_in', None) #pops 'True' value off and replace with None
    print ("route = ask")
    return render_template('ask.html',  error=error)




def return_home():  
    return redirect(url_for('Home')) #find a better redirect?

