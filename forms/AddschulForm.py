from flask_wtf import FlaskForm
from wtforms.fields.datetime import DateField
from wtforms.fields.simple import BooleanField, StringField, TextAreaField
from wtforms.fields import DecimalField
from wtforms import validators

class AddSchulForm(FlaskForm):
    Adresse = StringField("Adresse", validators = [validators.InputRequired()])
    Anzahl_Schüler = DecimalField("Anzahl Schüler", validators = [validators.InputRequired()])
    Name_Schule = StringField("Name Schule", validators = [validators.InputRequired()])
    Schulart = StringField("Schulart", validators = [validators.InputRequired()])
