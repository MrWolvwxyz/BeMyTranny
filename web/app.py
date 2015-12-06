from flask import Flask, render_template
import controllers
from extensions import mysql
app = Flask(__name__, template_folder='templates')

app.register_blueprint(controllers.ask)
app.register_blueprint(controllers.explorepage)
app.register_blueprint(controllers.main)
app.register_blueprint(controllers.login)
app.register_blueprint(controllers.userpage)


app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='zhouliyuan'
app.config['MYSQL_DB']='bmt'
mysql.init_app(app)
# comment this out using a WSGI like gunicorn
# if you dont, gunicorn will ignore it anyway
if __name__ == '__main__':
    # listen on external IPs
    app.run(host='localhost', port=5000, debug=True)