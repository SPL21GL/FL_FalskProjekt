from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField


class OrderdetailDeleteForm(FlaskForm):
    Vorname = StringField("Vorname")
    Nachname = StringField("Nachname")