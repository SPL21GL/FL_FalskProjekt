from flask.templating import render_template
from flask import Blueprint
from flask import request, Response
from functools import wraps
from models import db, User

index_blueprint = Blueprint('index_blueprint', __name__)


def check(username, password):
    user = db.session.query(User).filter(
        User.username == username and User.password == password).all()
    if user:
        return True
    else:
        return False


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


@index_blueprint.route("/", methods=["get", "post"])
@requires_auth
def return_base():
    return render_template("base.html")
