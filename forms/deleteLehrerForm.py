from flask_wtf import FlaskForm
from wtforms.fields.simple import HiddenField


class DeleteLehrerForm(FlaskForm):
    Lehrer_Id = HiddenField("Lehrer_Id")
