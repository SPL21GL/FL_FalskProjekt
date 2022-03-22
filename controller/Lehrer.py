from flask import Flask,request,redirect,flash
from flask.templating import render_template
from flask import Blueprint
import sqlalchemy
from models import db,Lehrer
from forms.addLehrerForm import AddLehrerForm
from forms.deleteLehrerForm import DeleteLehrerForm

lehrer_blueprint = Blueprint('lehrer_blueprint', __name__)

@lehrer_blueprint.route("/lehrer")
def index():
    session : sqlalchemy.orm.scoping.scoped_session = db.session
    lehrer = session.query(Lehrer).all()
    return render_template("lehrer.html", items = lehrer)

@lehrer_blueprint.route("/lehrer/add", methods=["GET","POST"])
def addLehrerForm():
    session : sqlalchemy.orm.scoping.scoped_session = db.session
    teacher = session.query(Lehrer).order_by(Lehrer.Lehrer_Id).all()
    
    adDTeacherForm = AddLehrerForm()

    if request.method == 'POST':
        
        if adDTeacherForm.validate_on_submit():
            print("gültig")

             #post kam zurück und ist valide
            
            print(adDTeacherForm.Vorname.data)
            print(adDTeacherForm.Nachname.data)
            print(adDTeacherForm.Faecher_Unterrichtet.data)
            print(adDTeacherForm.Anzahl_Klassen.data)
            #hier in DB Speichern
            
            newItem = Lehrer()
            newItem.Vorname = adDTeacherForm.Vorname.data
            newItem.Nachname = adDTeacherForm.Nachname.data
            newItem.Faecher_Unterrichtet = adDTeacherForm.Faecher_Unterrichtet.data
            newItem.Anzahl_Klassen = adDTeacherForm.Anzahl_Klassen.data

            db.session.add(newItem)
            db.session.commit()
            return redirect("/lehrer")
           
        else:
            raise "Fatal"
    else:
         return render_template("lehrer_add.html",Lehrer=Lehrer,form = adDTeacherForm)
    

@lehrer_blueprint.route("/lehrer/delete", methods=["post"])
def deleteLehrer():
    deleteLehrerformObj = DeleteLehrerForm()
    if deleteLehrerformObj.validate_on_submit():
        print("gültig")
        #db objekt holen
        #delete command ausführen

        itemIdToDelete = deleteLehrerformObj.Lehrer_Id.data
        itemToDelete = db.session.query(Lehrer).filter(Lehrer.Lehrer_Id == itemIdToDelete)
        itemToDelete.delete()
        
        db.session.commit()
    else:
        print("Fatal Error")
    
    flash(f"Item with id {itemIdToDelete} has been deleted")    

    return redirect("/lehrer")