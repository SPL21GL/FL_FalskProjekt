from flask_wtf import FlaskForm
from wtforms.fields.simple import HiddenField

class DeleteSchulForm(FlaskForm):
    school_Id = HiddenField("school_Id")