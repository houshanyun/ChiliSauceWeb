from flask import render_template, redirect, url_for, request, flash
from chiliweb import app, db
from chiliweb.models import Buylist, Admin

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/buy', methods=['GET', 'POST'])
def buy():
    if request.method == 'POST':        
        name = request.form['name']
        address = request.form['address']
        phone = request.form['phone']
        email = request.form['email']
        quantity = request.form['quantity']
        if not name or not address or not phone or not email or not quantity:
            flash('你有位輸入的資料喔!')
            return redirect(url_for('buy')) 

        buylist = Buylist(name=name, address=address, phone=phone, email=email, quantity=quantity)
        db.session.add(buylist)
        db.session.commit()
        flash('已送出訂單!')
        return redirect(url_for('index'))

    return render_template('buy.html')