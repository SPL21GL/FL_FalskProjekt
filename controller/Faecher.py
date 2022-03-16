from flask import Flask,request
from flask.templating import render_template
from flask import Blueprint
import sqlalchemy
from models import Faecher, db,School
from forms.addFaecherForm import AddFaecherForm

faecher_blueprint = Blueprint('faecher_blueprint', __name__)

@faecher_blueprint.route("/faecher")
def index():
    session : sqlalchemy.orm.scoping.scoped_session = db.session
    faecher = session.query(Faecher).all()
    return render_template("faecher.html", items = faecher)

@faecher_blueprint.route("/faecher/add", methods=["GET","POST"])
def addLehrerForm():
    session : sqlalchemy.orm.scoping.scoped_session = db.session
    faecher = session.query(Faecher).order_by(Faecher.Faecher_Id).all()
    
    adDFacherForm = AddFaecherForm()

    if request.method == 'POST':
        
        if adDFacherForm.validate_on_submit():
            print("gültig")

             #post kam zurück und ist valide
            
            print(adDFacherForm.Bezeichnung.data)
            print(adDFacherForm.Farbe.data)
            print(adDFacherForm.description.data)
            print(adDFacherForm.Lehrraum.data)
            #hier in DB Speichern
            
            newItem = Faecher()
            newItem.Bezeichnung = adDFacherForm.Bezeichnung.data
            newItem.Farbe = adDFacherForm.Farbe.data
            newItem.description = adDFacherForm.description.data
            newItem.Lehrraum = adDFacherForm.Lehrraum.data

            db.session.add(newItem)
            db.session.commit()
            return render_template("faecher_add.html",Faecher=Faecher, form = adDFacherForm)
        else:
            raise "Fatal"
    else:
        return render_template("faecher_add.html",Faecher=Faecher,form = adDFacherForm)