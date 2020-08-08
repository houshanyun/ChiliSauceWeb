from chiliweb import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Buylist(db.Model):
    __tablename__='buylist'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    phone = db.Column(db.Integer)
    address = db.Column(db.String(120))
    email = db.Column(db.String(50))
    quantity = db.Column(db.Integer)
    nowtime = db.Column(db.DateTime, default=datetime.utcnow, index=True)

class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def validate_password(self, password):
        return check_password_hash(self.password_hash, password)




