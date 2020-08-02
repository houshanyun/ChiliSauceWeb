from chiliweb import db
from datetime import datetime

class Buylist(db.Model):
    __tablename__='buylist'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    phone = db.Column(db.Integer)
    address = db.Column(db.String(120))
    quantity = db.Column(db.Integer)
    nowtime = db.Column(db.DateTime, default=datetime.utcnow, index=True)



