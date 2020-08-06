import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment
from flask_login import LoginManager


#import pymysql

#pymysql.install_as_MySQLdb()

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'gsfi34789hufds')
#app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{os.getenv('USER')}:{os.getenv('PASSWORD')}@127.0.0.1:3306/data"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.dirname(app.root_path), os.getenv('DATABASE_FILE', 'data.db'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(user_id):
    from chiliweb.models import Admin
    user = Admin.query.get(int(user_id))
    return user

login_manager.login_view = 'index'

from chiliweb import views, commands
