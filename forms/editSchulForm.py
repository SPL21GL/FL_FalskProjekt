from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, HiddenField
from wtforms.fields import DecimalField


class EditSchulForm(FlaskForm):
    school_Id = HiddenField("school_Id")
    Adresse = StringField("Adresse")
    Anzahl_Schueler = DecimalField("Anzahl_Schüler")
    Name_Schule = StringField("Name_Schule")
    Schulart = StringField("Schulart")
