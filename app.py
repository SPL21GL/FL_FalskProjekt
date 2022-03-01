from flask import Flask
from flask.templating import render_template
from models import db


app = Flask(__name__)
app.secret_key = "VerySecretSecretKey"


app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost/todoItemApp"
db.init_app(app)

@app.route("/", methods=["get","post"])
def index():
    return render_template("index.html",headline = "SchulDb")

app.run(debug=True)