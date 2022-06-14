from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField
from wtforms.fields import DecimalField, SelectField,HiddenField


class OrderdetailForm(FlaskForm):
    school_Id = HiddenField("school_Id")
    Lehrer_Id = SelectField("Lehrer_Id")
                            