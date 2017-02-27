from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, RadioField
from wtforms.validators import DataRequired, Length

class StoreForm(FlaskForm):
    store_name = StringField('store_name', validators=[DataRequired()])
    # address = TextAreaField('address', [validators.required(), validators.length(max=200)])
    address = TextAreaField('address', validators=[DataRequired()])
    phone = StringField('phone', validators=[Length(min=0,max=15)])
    cuisine_type = StringField('cuisine_type', validators=[Length(min=0,max=50)])
    opening_time = StringField('opening_time', validators=[Length(min=0,max=15)])
    closing_time = StringField('closing_time', validators=[Length(min=0,max=15)])


class MenuForm(FlaskForm):
    category = StringField('cuisine_type', validators=[Length(min=0,max=80)])
    # gave the RadioField the old college try :(
    # category = RadioField('Label', choices=[('1','Breakfast'),
    #                      ('2','Lunch'),('3','Dinner')])

class ItemForm(FlaskForm):
    item_name = StringField('item_name', validators=[DataRequired()])
    description = StringField('description', validators=[DataRequired()])
    section =  StringField('section', validators=[DataRequired()])
    price =  StringField('price', validators=[DataRequired()])
