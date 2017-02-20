from flask_wtf import Form
from wtforms import StringField, TextAreaField, RadioField
from wtforms.validators import DataRequired, Length

class StoreForm(Form):
    store_name = StringField('store_name', validators=[DataRequired()])
    # address = TextAreaField('address', [validators.required(), validators.length(max=200)])
    address = TextAreaField('address', validators=[DataRequired()])
    phone = StringField('phone', validators=[Length(min=0,max=15)])
    cuisine_type = StringField('cuisine_type', validators=[Length(min=0,max=50)])
    opening_time = StringField('opening_time', validators=[Length(min=0,max=15)])
    closing_time = StringField('closing_time', validators=[Length(min=0,max=15)])


    # store_name = db.Column(db.String(64), index=True, unique=True)
    # address = db.Column(db.String(200), index=True, unique=True)
    # phone = db.Column(db.String(15))
    # cuisine_type = db.Column(db.String(50))
    # opening_time = db.Column(db.String(15))
    # closing_time = db.Column(db.String(15))
