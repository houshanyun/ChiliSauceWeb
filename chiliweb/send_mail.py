from threading import Thread

from flask_mail import Message, Mail

from chiliweb.models import Buylist
from chiliweb import app, mail

def sendMail():

    txt = Buylist.query.order_by(Buylist.nowtime.desc()).all()
    name = txt[0].name
    phone = txt[0].phone
    address = txt[0].address
    email = txt[0].email
    quantity = txt[0].quantity
    time = txt[0].nowtime
    m_title = '有人下單了!'
    m_mymail = ['nigellin.1008@gmail.com']
    m_html = \
    f'''
    <p>客戶姓名 : {name}</p>
    <p>手機 : {phone}</p>
    <p>住址 : {address}</p>
    <p>電子信箱 : {email}</p>
    <p>訂購數量 : {quantity}</p>
    <p>下單時間 : {time}</p>
    '''

    msg = Message(
        m_title,
        recipients=m_mymail
        )
    msg.html = m_html

    # 多線呈
    thr = Thread(target=async_mail, args=[app, msg])
    thr.start()

# 你必需讓程序是在相同的Context內，
# 因此需要也必需利用app.app_context來確保線程。
def async_mail(app, msg):
    with app.app_context():
        mail.send(msg)


