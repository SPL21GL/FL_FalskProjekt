from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, TextAreaField, HiddenField


class EditFaecherForm(FlaskForm):
    Faecher_Id = HiddenField("Faecher_Id")
    Bzeichnung = StringField("Bzeichnung")
    Farbe = TextAreaField("Farbe")
    description = StringField("description")
    Lehrraum = StringField("Lehrraum")
