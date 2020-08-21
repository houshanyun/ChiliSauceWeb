import click

from chiliweb import app, db
from chiliweb.models import Admin, Buylist

@app.cli.command()
@click.option('--drop', is_flag=True, help='create db')
def  initdb(drop):
    if drop:
        db.drop_all()
    db.create_all()
    click.echo('重置資料庫')

@app.cli.command()
@click.option('--username', prompt=True, help='login system')
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True, help='user to login')
def admin(username, password):
    
    db.create_all()

    user = Admin.query.first()
    if user:
        click.echo('更新帳號...')
        user.username = username
        user.set_password(password)
    else:
        click.echo('創造帳號...')
        user = Admin(username=username)
        user.set_password(password)
        db.session.add(user)
        
    db.session.commit()
    click.echo('Done')


@app.cli.command()
@click.option('--count', default=20, help='faker')
def forge(count):

    from faker import Faker

    db.drop_all()
    db.create_all()

    fake = Faker('zh_tw')
    click.echo('資料生成中...')

    for _ in range(count):
        test_list = Buylist(
            name = fake.name(),
            phone= fake.phone_number(),
            address = fake.address(),
            email = fake.email(),
            quantity = fake.random_digit()
        )
        db.session.add(test_list)
    
    db.session.commit()
    click.echo('資料完成...')
