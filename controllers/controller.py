from flask import render_template, request, redirect
from app import app
from models.item import *
from models.items import *

@app.route('/items')
def index():
    items = list_of_items
    apply_discount(items)
    total_items = total_number(items)
    total = total_cost_items(items)
    return render_template('index.html', title='Shopping list', items=items, total=total, total_items=total_items)

@app.route('/items/bought')
def bought():
    items = show_bought(list_of_items)
    apply_discount(items)
    total_items = total_number(items)
    total = total_cost_items(items)
    return render_template('index.html', title='Shopping list', items=items, total=total, total_items=total_items)

@app.route('/items/to_buy')
def to_buy():
    items = show_not_bought(list_of_items)
    apply_discount(items)
    total_items = total_number(items)
    total = total_cost_items(items)
    return render_template('index.html', title='Shopping list', items=items, total=total, total_items=total_items)


@app.route('/items', methods=['POST'])
def add_item():
    name_of_item = request.form['name_of_item']
    price_of_item = request.form['price_of_item']
    quantity = request.form['quantity']
    bought_status = True if 'bought_status' in request.form else False
    newitem = Item(name_of_item, price_of_item, quantity, bought_status)
    add_new_item(newitem)
    return redirect('/items')

@app.route('/items/delete/<item_name>', methods=['POST'])
def delete(item_name):
    delete_item(item_name)
    return redirect('/items')






