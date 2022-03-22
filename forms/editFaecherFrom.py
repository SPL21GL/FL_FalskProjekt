from flask_wtf import FlaskForm
from wtforms.fields.datetime import DateField
from wtforms.fields.simple import BooleanField, StringField, TextAreaField, HiddenField

class EditFaecherForm(FlaskForm):
    Faecher_Id = HiddenField("Faecher_Id")
    Bezeichnung = StringField("Bezeichnung")
    Farbe = TextAreaField("Farbe")
    describtion = DateField("describtion")
    Lehrraum = StringField("Lehrraum")