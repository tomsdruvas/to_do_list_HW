from flask import render_template
from app import app
from models.item import *
from models.items import *

@app.route('/items')
def index():
    return render_template('index.html', title='Shopping list', items=items)
