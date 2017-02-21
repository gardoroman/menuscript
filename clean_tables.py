from app import db, models
stores = models.Store.query.all()
for s in stores:
    db.session.delete(s)
menus = models.Menu.query.all()
for m in menus:
    db.session.delete(m)
db.session.commit()
items = models.Item.query.all()
for i in items:
    db.session.delete(i)
db.session.commit()
