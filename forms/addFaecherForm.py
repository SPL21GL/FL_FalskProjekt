from flask_wtf import FlaskForm
from wtforms.fields.datetime import DateField
from wtforms.fields.simple import BooleanField, StringField, TextAreaField
from wtforms.fields import DecimalField
from wtforms import validators

class AddFaecherForm(FlaskForm):
    Bzeichnung = StringField("Bezeichnung", validators = [validators.InputRequired()])
    Farbe = StringField("Farbe", validators = [validators.InputRequired()])
    description = StringField("description", validators = [validators.InputRequired()])
    Lehrraum = DecimalField("Lehrraum", validators = [validators.InputRequired()])
