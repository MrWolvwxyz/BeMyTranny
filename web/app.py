from flask import Flask, render_template
import controllers
import sys
from extensions import mysql
app = Flask(__name__, template_folder='templates')

app.register_blueprint(controllers.ask)
app.register_blueprint(controllers.explorepage)
app.register_blueprint(controllers.main)
app.register_blueprint(controllers.login)
app.register_blueprint(controllers.userpage)
app.register_blueprint(controllers.addmoreresponse)
app.register_blueprint(controllers.logout)


app.config['MYSQL_USER']='root'
try:
    pw = str(sys.argv[1]) #password supplied as cmd line arg
except:
    pw = str(raw_input("input mysql password:")) #or input later
app.config['MYSQL_PASSWORD']=pw
app.config['MYSQL_DB']='bmt'
app.secret_key = '\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8'
mysql.init_app(app)
# comment this out using a WSGI like gunicorn
# if you dont, gunicorn will ignore it anyway
if __name__ == '__main__':
    # listen on external IPs
    app.run(host='localhost', port=5000, debug=True)
