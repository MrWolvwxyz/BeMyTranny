from flask import *
from hashlib import sha256
from extensions import mysql
import os

fakeloggedin = True
fakeuserid = 12345

ask = Blueprint('ask', __name__, template_folder='templates')

picAdded = False

@ask.route('/ask',  methods=['GET', 'POST'])
def askfunc():
    error = None
    if request.method=='POST':
        op=request.form['op']
        print ("enter the post")
        if op == "submit":

            newpic = request.files['photo']
            picAdded = True;
            currentuserid = 1;
            currentuserid = str(currentuserid)
            newpic.save("static/pictures/"  + currentuserid +   "/" +newpic.filename)

            title = request.form['title']
            ori = request.form['ori']
            tar = request.form['tar']
            des = request.form['des']
            cur=mysql.connection.cursor()
            cur.execute("insert into post (title, description, origin, target, pathtophoto, userid) values ('" + title + "', '" + des + "', '" + ori + "', '" + tar + "', '" + newpic.filename +"', "+ currentuserid +");")
            cur.execute("commit")

        return render_template('ask.html',  error=error)

    print ("route = ask")

    return render_template('ask.html',  error=error)






