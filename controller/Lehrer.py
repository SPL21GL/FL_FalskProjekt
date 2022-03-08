from flask import Flask
from flask.templating import render_template
from flask import Blueprint
import sqlalchemy
from models import db,Lehrer

lehrer_blueprint = Blueprint('school_blueprint', __name__)

@lehrer_blueprint.route("/lehrer")
def index():
    session : sqlalchemy.orm.scoping.scoped_session = db.session
    schools = session.query(School).all()
    return render_template("schul.html", items = schools)
