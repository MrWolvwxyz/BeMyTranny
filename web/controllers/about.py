from flask import *
from hashlib import sha256

from extensions import mysql

fakeloggedin = True
fakeuserid = 12345

about = Blueprint('about', __name__, template_folder='templates')


@about.route('/about', methods=['GET', 'POST'])
def aboutfunc():
	return render_template('about.html')




