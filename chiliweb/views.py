from flask import render_template, redirect, url_for, request, flash
from chiliweb import app, db
from chiliweb.models import Buylist

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')