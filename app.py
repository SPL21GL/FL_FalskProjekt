from flask import Flask
import sqlalchemy
from models import db
from controller.index import index_blueprint
from controller.schule import school_blueprint
from controller.Lehrer import lehrer_blueprint
from controller.Faecher import faecher_blueprint
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)
app.secret_key = "VerySecretSecretKey"

csrf = CSRFProtect(app)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost/Schule"
db.init_app(app)

session: sqlalchemy.orm.scoped_session = db.session


app.register_blueprint(school_blueprint)
app.register_blueprint(lehrer_blueprint)
app.register_blueprint(faecher_blueprint)
app.register_blueprint(index_blueprint)
app.run(debug=True)
