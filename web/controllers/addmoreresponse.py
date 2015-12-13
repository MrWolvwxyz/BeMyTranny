from flask import *
from hashlib import sha256

from extensions import mysql

fakeloggedin = False
fakeuserid = 12345

addmoreresponse = Blueprint('addmoreresponse', __name__, template_folder='templates')


@addmoreresponse.route('/addmoreresponse/<postID>', methods=['GET', 'POST'])
def addmoreresponsefunc(postID):
	options=\
	{
		"login": False,
		"username": "",
		"status": 0
	}
	error = None
	if session.has_key('username'):
		options["login"]=True
		options["username"]=session["username"]
	else:
		return render_template('errorpage.html', error = error)


	postID = str(postID)

	if request.method == 'GET':

		cur=mysql.connection.cursor()
		postID = str(postID)
		cur.execute("select * from post where postid = " + postID)
		msgs = [];

		msgs=cur.fetchall()
		post = msgs[0]

		cur=mysql.connection.cursor()
		cur.execute("select * from answer where postid = " + postID)
		answers = [];

		answers=cur.fetchall()

		

		index = []
		indexcount = 0
		names = []


		for a in answers:
			cur=mysql.connection.cursor()
			userid = str(a[2])
			cur.execute("select username from user where userid = " + userid)
			name = [];

			name=cur.fetchall()

			names.append(name)
			index.append(indexcount)
			indexcount = indexcount + 1



		return render_template('addmoreresponse.html', post = post, answer = answers, name = names, index = index, **options)
	
	if request.method=='POST':

		op=request.form['op']
		
		if op == "submit":
			des = request.form['ans']
			cur=mysql.connection.cursor()
			userid = 1
			userid = str(userid)


			cur.execute("insert into answer (detail, userid, postid) values ('" + des + "', '" + userid + "', '" + postID + "');")
			cur.execute("commit")


        return render_template('redirect.html',  error=error)
	


	return render_template('addmoreresponse.html', error = error, **options)







