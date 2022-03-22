from flask import Flask,request, flash, redirect
from flask.templating import render_template
from flask import Blueprint
import sqlalchemy
from models import db,School
from forms.addSchulForm import AddSchulForm
from forms.deleteSchulForm import DeleteSchulForm


school_blueprint = Blueprint('school_blueprint', __name__)

@school_blueprint.route("/schule")
def index():
    session : sqlalchemy.orm.scoping.scoped_session = db.session
    schools = session.query(School).all()
    return render_template("schoolHTML/schul.html", items = schools)


@school_blueprint.route("/school/add", methods=["GET","POST"])
def schools_add():
    session : sqlalchemy.orm.scoping.scoped_session = db.session
    school = session.query(School).order_by(School.school_Id).all()
    
    adDSchulForm = AddSchulForm()

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
            return redirect("/schule")
           
        
        else:
            raise "Fatal"
    else:
         return render_template("schoolHTML/schul_add.html",school=school,form = adDSchulForm)
    

#delete

@school_blueprint.route("/schul/delete", methods=["post"])
def deleteSchul():
    deleteSchulformObj = DeleteSchulForm()
    if deleteSchulformObj.validate_on_submit():
        print("gültig")
        #db objekt holen
        #delete command ausführen

        itemIdToDelete = deleteSchulformObj.school_Id.data
        itemToDelete = db.session.query(School).filter(School.school_Id == itemIdToDelete)
        itemToDelete.delete()
        
        db.session.commit()
    else:
        print("Fatal Error")
    
    flash(f"Item with id {itemIdToDelete} has been deleted")    

    return redirect("/schule")