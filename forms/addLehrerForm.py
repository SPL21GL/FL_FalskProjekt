from flask_wtf import FlaskForm
from wtforms.fields.datetime import DateField
from wtforms.fields.simple import BooleanField, StringField, TextAreaField
from wtforms.fields import DecimalField
from wtforms import validators

class AddLehrerForm(FlaskForm):
    Vorname = StringField("Adresse", validators = [validators.InputRequired()])
    Nachname = StringField("Anzahl Schüler", validators = [validators.InputRequired()])
    Faecher_Unterrichtet = StringField("Name Schule", validators = [validators.InputRequired()])
    Anzahl_Klassen = DecimalField("Schulart", validators = [validators.InputRequired()])
