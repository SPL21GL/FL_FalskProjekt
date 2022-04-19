from flask import Flask
from flask.templating import render_template
from flask import Blueprint
import sqlalchemy
from models import db
from flask import Flask, request, jsonify, Response
from flask import Blueprint
from functools import wraps


index_blueprint = Blueprint('index_blueprint', __name__)

def check(username, password):
    return username == "admin" and password == "3bhwii1"

def auth():
    return Response('Please login!', 401, {'WWW-Authenticate': 'Basic real="Login Required"'})

def requires_auth(f):
    @wraps(f)
    def deco(*args, **kwargs):
        autho = request.authorization
        if not autho or not check(autho.username, autho.password):
            return auth()
        return f(*args, ** kwargs)
    return deco

@index_blueprint.route("/", methods=["get","post"])
@requires_auth
def return_base():
    return render_template("base.html")

