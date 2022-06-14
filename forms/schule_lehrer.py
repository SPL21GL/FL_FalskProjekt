from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField
from wtforms.fields import DecimalField, SelectField


class OrderdetailForm(FlaskForm):
    Nachname = SelectField("Nachname")
                            