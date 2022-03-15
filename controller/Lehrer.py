from flask import Flask
from flask.templating import render_template
from flask import Blueprint
import sqlalchemy
from models import db,Lehrer

lehrer_blueprint = Blueprint('lehrer_blueprint', __name__)

@lehrer_blueprint.route("/lehrer")
def index():
    session : sqlalchemy.orm.scoping.scoped_session = db.session
    lehrer = session.query(Lehrer).all()
    return render_template("lehrer.html", items = lehrer)
