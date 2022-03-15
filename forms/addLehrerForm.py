from flask_wtf import FlaskForm
from wtforms.fields.datetime import DateField
from wtforms.fields.simple import BooleanField, StringField, TextAreaField
from wtforms.fields import DecimalField
from wtforms import validators

class AddLehrerForm(FlaskForm):
    Vorname = StringField("Adresse")
    Nachname = StringField("Anzahl Schüler")
    Faecher_Unterrichtet = StringField("Name Schule")
    Anzahl_Klassen = DecimalField("Schulart")
