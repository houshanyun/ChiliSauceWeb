import click

from chiliweb import app, db
from chiliweb.models import Buylist

@app.cli.command()
@click.option('--drop', is_flag=True, help='create db')
def  initdb(drop):
    if drop:
        db.drop_all()
    db.create_all()
    click.echo('重置資料庫')
