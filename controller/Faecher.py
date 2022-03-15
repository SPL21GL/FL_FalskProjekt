from flask import Flask
from flask.templating import render_template
from flask import Blueprint
import sqlalchemy
from models import Faecher, db,School

faecher_blueprint = Blueprint('faecher_blueprint', __name__)

@faecher_blueprint.route("/faecher")
def index():
    session : sqlalchemy.orm.scoping.scoped_session = db.session
    faecher = session.query(Faecher).all()
    return render_template("faecher.html", items = faecher)

