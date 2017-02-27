from flask import render_template, redirect, session, url_for, flash, request
from app import app, db
from .models import Store, Menu, Item
from .forms import StoreForm, MenuForm, ItemForm

# view for all stores
@app.route('/')
@app.route('/index')
def index():
    stores = Store.query.all()
    return render_template('index.html',
                            stores=stores)

@app.route('/stores/<store_name>')
def stores(store_name):
    store = Store.query.filter_by(store_name=store_name).first()
    if store is None:
        flash('Store %s not found.' % store_name)
        return redirect(url_for('index'))
    return render_template('store.html', store=store)

@app.route('/stores/<int:store_id>/menus/<int:menu_id>')
def menus(store_id, menu_id):
    menu = Menu.query.get(int(menu_id))
    store = Store.query.get(menu.store_id)
    if menu is None:
        flash('Menu %s not found.' % menu_id)
        return redirect(url_for('index'))
    return render_template('menu.html', menu=menu, store=store)

# route for updating Store
# @app.route('/stores/new', methods=['GET', 'POST'])
@app.route('/stores/new')
def new_store():
    form = StoreForm()
    return render_template('new_store.html', form=form)

@app.route('/stores', methods=['POST'])
def create_store():
    form = StoreForm()
    if form.validate_on_submit():
        # there has to be a better way to update
        new_store = Store(store_name=request.form['store_name'],
                address=request.form['address'],phone=request.form['phone'],
                cuisine_type=request.form['cuisine_type'],opening_time=request.form['opening_time'],
                closing_time=request.form['closing_time'])
        db.session.add(new_store)
        db.session.commit()
        return redirect(url_for('stores', store_name=new_store.store_name))
    return render_template('new_store.html', form=form)

@app.route('/stores/<int:store_id>/menus/new')
def new_menu(store_id):
    form = MenuForm()
    return render_template('new_menu.html', form=form, store_id=store_id)

@app.route('/stores/<int:store_id>/menus', methods=['POST'])
def create_menu(store_id):
    form = MenuForm()
    menu = Menu(store_id=store_id)
    cat = request.form['category']
    if cat.strip() != '' and form.validate_on_submit():
        menu.category = cat
        db.session.add(menu)
        db.session.commit()
        return redirect(url_for('menus', store_id=store_id, menu_id=menu.id))
    return render_template('new_menu.html', form=form, store_id=store_id)

@app.route('/stores/<int:store_id>/menus/<int:menu_id>/items/new')
def new_item(store_id, menu_id):
    form = ItemForm()
    return render_template('new_item.html', form=form, store_id=store_id, menu_id=menu_id)

@app.route('/stores/<int:store_id>/menus/<int:menu_id>/items', methods=['POST'])
def create_item(store_id, menu_id):
    form = ItemForm()
    item = Item(menu_id=menu_id)
    if form.validate_on_submit():
        item.item_name = request.form['item_name']
        item.description = request.form['description']
        item.section = request.form['section']
        item.price = request.form['price']
        db.session.add(item)
        db.session.commit()
        return redirect(url_for('menus', store_id=store_id, menu_id=menu_id))
    return render_template('new_item.html', form=form, store_id=store_id, menu_id=menu_id)
