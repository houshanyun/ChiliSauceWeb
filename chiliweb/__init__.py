import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment
from flask_login import LoginManager
from flask_mail import Mail

#import pymysql

#pymysql.install_as_MySQLdb()

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'gsfi34789hufds')
#app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{os.getenv('USER')}:{os.getenv('PASSWORD')}@127.0.0.1:3306/data"
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.dirname(app.root_path), os.getenv('DATABASE_FILE', 'data.db'))
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://mxstiuaxibfxyh:f5570063166016f79dc1d38fb21897910d757892acad72506448d6a744db5d51@ec2-35-175-155-248.compute-1.amazonaws.com:5432/d2q1biiblsoihg'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER')

db = SQLAlchemy(app)
moment = Moment(app)
mail = Mail(app)
login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(user_id):
    from chiliweb.models import Admin
    user = Admin.query.get(int(user_id))
    return user

login_manager.login_view = 'index'

from chiliweb import views, commands
