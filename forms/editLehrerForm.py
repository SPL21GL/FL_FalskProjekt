from flask_wtf import FlaskForm
from wtforms.fields.datetime import DateField
from wtforms.fields.simple import BooleanField, StringField, TextAreaField, HiddenField
from wtforms.fields import DecimalField

class EditLehrerForm(FlaskForm):
    Lehrer_Id = HiddenField("Lehrer_Id")
    Vorname = StringField("Vorname")
    Nachname = StringField("Nachname")
    Faecher_Unterrichtet = StringField("Faecher_Unterrichtet")
    Anzahl_Klassen = DecimalField("Anzahl_Klassen")