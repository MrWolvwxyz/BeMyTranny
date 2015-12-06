from flask import *
from hashlib import sha256

from extensions import mysql

fakeloggedin = True
fakeuserid = 12345

explorepage = Blueprint('explorepage', __name__, template_folder='templates')


@explorepage.route('/explorepage')
def explorepagefunc():
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




