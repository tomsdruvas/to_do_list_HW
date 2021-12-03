from flask import render_template, request, redirect
from app import app
from models.item import *
from models.items import *

@app.route('/items')
def index():
    return render_template('index.html', title='Shopping list', items=items)


@app.route('/items', methods=['POST'])
def add_item():
    name_of_item = request.form['name_of_item']
    price_of_item = int(request.form['price_of_item'])
    quantity = int(request.form['quantity'])
    bought_status = True if 'bought_status' in request.form else False
    newitem = Item(name_of_item, price_of_item, quantity, bought_status)
    add_new_item(newitem)
    return redirect('/items')







