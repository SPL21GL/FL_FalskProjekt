from flask import Flask
from flask.templating import render_template
from flask import Blueprint
import sqlalchemy
from models import db

index_blueprint = Blueprint('index_blueprint', __name__)


@index_blueprint.route("/", methods=["get","post"])
def index():
    return render_template("index.html",headline = "SchulDb")

