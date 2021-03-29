from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, SelectMultipleField, FileField, FieldList, FormField


class NewCity(FlaskForm):
    zipcode = StringField('Zipcode')