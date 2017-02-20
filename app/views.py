from flask import render_template, redirect, session, url_for, flash
from app import app, db
from .models import Store, Menu, Item

# view for all stores
@app.route('/')
@app.route('/index')
def index():
    stores = Store.query.all()
    return render_template('index.html',
                            stores=stores)

@app.route('/store/<store_name>')
def store(store_name):
    store = Store.query.filter_by(store_name=store_name).first()
    if store is None:
        flash('Store %s not found.' % store_name)
        return redirect(url_for('index'))
    return render_template('store.html', store=store)

@app.route('/menu/<menu_id>')
def menu(menu_id):
    menu = Menu.query.get(int(menu_id))
    store = Store.query.get(menu.store_id)
    if menu is None:
        flash('Menu %s not found.' % menu_id)
        return redirect(url_for('index'))
    return render_template('menu.html', menu=menu, store=store)
