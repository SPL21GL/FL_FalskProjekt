from flask import Flask
from flask.templating import render_template
import sqlalchemy
from models import db
from controller.index import index_blueprint
from controller.schule import school_blueprint


app = Flask(__name__)
app.secret_key = "VerySecretSecretKey"


app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost/Schule"
db.init_app(app)

session : sqlalchemy.orm.scoped_session = db.session

app.register_blueprint(school_blueprint)
app.register_blueprint(index_blueprint)
app.run(debug=True)