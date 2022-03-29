from flask_wtf import FlaskForm
from wtforms.fields.datetime import DateField
from wtforms.fields.simple import BooleanField, StringField, TextAreaField, HiddenField

class EditFaecherForm(FlaskForm):
    Faecher_Id = HiddenField("Faecher_Id")
    Bzeichnung = StringField("Bzeichnung")
    Farbe = TextAreaField("Farbe")
    description = StringField("description")
    Lehrraum = StringField("Lehrraum")