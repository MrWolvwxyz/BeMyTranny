from app import app
from flask import render_template
from .forms import LoginForm

@app.route('/')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html', 
                           title='Sign In',
                           form=form)

@app.route('/index')
def index():
    return render_template('index.html',
                           title='Home')