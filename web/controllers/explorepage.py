from flask import *
from hashlib import sha256

from extensions import mysql

fakeloggedin = True
fakeuserid = 12345

explorepage = Blueprint('explorepage', __name__, template_folder='templates')


@explorepage.route('/explorepage')
def explorepagefunc():
    if request.method == 'GET':
    	print(session['username'])
        cur=mysql.connection.cursor()
        cur.execute("select * from post")
        msgs = [];
        msgs=cur.fetchall()

        print ("this is a get method") 
    return render_template('explorepage.html', data = msgs)




