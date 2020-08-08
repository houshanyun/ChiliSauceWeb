from flask import render_template, redirect, url_for, request, flash
from chiliweb import app, db
from chiliweb.models import Buylist, Admin
from flask_login import login_user, login_required, logout_user, current_user

from chiliweb import send_mail

from datetime import datetime

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
            flash('你有沒輸入的資料...')
            return redirect(url_for('buy')) 
        buylist = Buylist(name=name, address=address, phone=phone, email=email, quantity=quantity)
        db.session.add(buylist)
        db.session.commit()
        flash('已送出訂單...')
        send_mail.sendMail()

        return redirect(url_for('index'))

    return render_template('buy.html')


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if current_user.is_authenticated:
        return  redirect('boss_page')
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if not username or not password:
            flash('請輸入正確數值...')
            return redirect(url_for('admin'))
        user = Admin.query.first()
        if username == user.username and user.validate_password(password):
            login_user(user)
            flash('老闆已登入...')
            return redirect(url_for('boss_page'))
        else:
            flash('帳號或密碼錯誤...')
            return redirect(url_for('admin'))
    return render_template('admin.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('goodbye...')
    return redirect(url_for('index'))

@app.route('/boss_page', methods=['GET'])
@login_required
def boss_page():
    all_buy = Buylist.query.order_by(Buylist.nowtime.desc()).all()
    return render_template('boss_page.html', mybuy=all_buy)
