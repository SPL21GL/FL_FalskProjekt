from flask_wtf import FlaskForm
from wtforms.fields.datetime import DateField
from wtforms.fields.simple import BooleanField, StringField, TextAreaField
from wtforms.fields import DecimalField
from wtforms import validators

class AddFaecherForm(FlaskForm):
    Bezeichnung = StringField("Bezeichnung")
    Farbe = StringField("Farbe")
    description = StringField("description")
    Lehrraum = DecimalField("Lehrraum")
