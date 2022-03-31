from flask_wtf import FlaskForm
from wtforms.fields.datetime import DateField
from wtforms.fields.simple import BooleanField, StringField, TextAreaField, HiddenField
from wtforms.fields import DecimalField

class EditSchulForm(FlaskForm):
    school_Id = HiddenField("school_Id")
    Adresse = StringField("Adresse")
    Anzahl_Schüler = DecimalField("Anzahl_Schüler")
    Name_Schule = StringField("Name_Schule")
    Schulart = StringField("Schulart")