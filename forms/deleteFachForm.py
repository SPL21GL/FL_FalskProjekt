from flask_wtf import FlaskForm
from wtforms.fields.simple import HiddenField


class DeleteFaecherForm(FlaskForm):
    Faecher_Id = HiddenField("Faecher_Id")
