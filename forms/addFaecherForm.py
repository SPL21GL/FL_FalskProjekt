from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField
from wtforms.fields import DecimalField
from wtforms import validators


class AddFaecherForm(FlaskForm):
    Bzeichnung = StringField("Bezeichnung", validators=[
                             validators.InputRequired()])
    Farbe = StringField("Farbe", validators=[validators.InputRequired()])
    description = StringField("description", validators=[
                              validators.InputRequired()])
    Lehrraum = DecimalField("Lehrraum", validators=[
                            validators.InputRequired()])
