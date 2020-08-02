import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment
import pymysql

pymysql.install_as_MySQLdb()

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'gsfi34789hufds')
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{os.getenv('USER')}:{os.getenv('PASSWORD')}@127.0.0.1:3306/data"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from chiliweb import views, commands
