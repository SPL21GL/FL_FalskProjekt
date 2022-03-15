from flask import Flask,request
from flask.templating import render_template
from flask import Blueprint
import sqlalchemy
from models import db,School
from forms.AddschulForm import addSchulForm

school_blueprint = Blueprint('school_blueprint', __name__)

@school_blueprint.route("/schule")
def index():
    session : sqlalchemy.orm.scoping.scoped_session = db.session
    schools = session.query(School).all()
    return render_template("schul.html", items = schools)


@school_blueprint.route("/school/add", methods=["GET","POST"])
def schools_add():
    session : sqlalchemy.orm.scoping.scoped_session = db.session
    school = session.query(School).order_by(School.school_Id).all()
    
    adDSchulForm = addSchulForm()

    if request.method == 'POST':
        
        if adDSchulForm.validate_on_submit():
            print("gültig")

             #post kam zurück und ist valide
            print(adDSchulForm.Adresse.data)
            print(adDSchulForm.Anzahl_Schüler.data)
            print(adDSchulForm.Name_Schule.data)
            print(adDSchulForm.Schulart.data)
            #hier in DB Speichern
            
            newItem = School()
            newItem.Adresse = adDSchulForm.Adresse.data
            newItem.Anzahl_Schüler = adDSchulForm.Anzahl_Schüler.data
            newItem.Name_Schule = adDSchulForm.Name_Schule.data
            newItem.Schulart = adDSchulForm.Schulart.data

            db.session.add(newItem)
            db.session.commit()
            return render_template("schul_add.html",school=school, form = adDSchulForm)
        else:
            raise "Fatal"
    else:
        return render_template("schul_add.html",school=school,form = adDSchulForm)