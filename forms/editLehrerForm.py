from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, HiddenField
from wtforms.fields import DecimalField


class EditLehrerForm(FlaskForm):
    Lehrer_Id = HiddenField("Lehrer_Id")
    Vorname = StringField("Vorname")
    Nachname = StringField("Nachname")
    Faecher_Unterrichtet = StringField("Faecher_Unterrichtet")
    Anzahl_Klassen = DecimalField("Anzahl_Klassen")
