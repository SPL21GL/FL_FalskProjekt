from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField
from wtforms.fields import DecimalField
from wtforms import validators


class AddSchulForm(FlaskForm):
    Adresse = StringField("Adresse", validators=[validators.InputRequired()])
    Anzahl_Schueler = DecimalField("Anzahl Schüler", validators=[
                                   validators.InputRequired()])
    Name_Schule = StringField("Name Schule", validators=[
                              validators.InputRequired()])
    Schulart = StringField("Schulart", validators=[validators.InputRequired()])
