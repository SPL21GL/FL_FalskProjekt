from flask import Flask,request,redirect,flash
from flask.templating import render_template
from flask import Blueprint
import sqlalchemy
from models import Faecher, db,School
from forms.addFaecherForm import AddFaecherForm
from forms.deleteFachForm import DeleteFaecherForm
from forms.editFaecherFrom import EditFaecehrFrom, EditFaecherForm


faecher_blueprint = Blueprint('faecher_blueprint', __name__)

@faecher_blueprint.route("/faecher")
def index():
    session : sqlalchemy.orm.scoping.scoped_session = db.session
    faecher = session.query(Faecher).all()
    return render_template("faecherHTML/faecher.html", items = faecher)

@faecher_blueprint.route("/faecher/add", methods=["GET","POST"])
def addLehrerForm():
    session : sqlalchemy.orm.scoping.scoped_session = db.session
    faecher = session.query(Faecher).order_by(Faecher.Faecher_Id).all()
    
    adDFacherForm = AddFaecherForm()

    if request.method == 'POST':
        
        if adDFacherForm.validate_on_submit():
            print("gültig")

             #post kam zurück und ist valide
            
            print(adDFacherForm.Bzeichnung.data)
            print(adDFacherForm.Farbe.data)
            print(adDFacherForm.description.data)
            print(adDFacherForm.Lehrraum.data)
            #hier in DB Speichern
            
            newItem = Faecher()
            newItem.Bzeichnung = adDFacherForm.Bzeichnung.data
            newItem.Farbe = adDFacherForm.Farbe.data
            newItem.description = adDFacherForm.description.data
            newItem.Lehrraum = adDFacherForm.Lehrraum.data

            db.session.add(newItem)
            db.session.commit()
            return redirect("/faecher")
        else:
            raise "Fatal"
    else:
        return render_template("faecherHTML/faecher_add.html",Faecher=Faecher,form = adDFacherForm)

@faecher_blueprint.route("/faecher/delete", methods=["post"])
def deleteFach():
    deleteLehrerformObj = DeleteFaecherForm()
    if deleteLehrerformObj.validate_on_submit():
        print("gültig")
        #db objekt holen
        #delete command ausführen

        itemIdToDelete = deleteLehrerformObj.Faecher_Id.data
        itemToDelete = db.session.query(Faecher).filter(Faecher.Faecher_Id == itemIdToDelete)
        itemToDelete.delete()
        
        db.session.commit()
    else:
        print("Fatal Error")
    
    flash(f"Item with id {itemIdToDelete} has been deleted")    

    return redirect("/faecher")

@faecher_blueprint.route("/faecher/edit",methods=["post"])
def submitEditForm():
    editItemFormObject = EditFaecherForm()

    if editItemFormObject.validate_on_submit():
        print("Submit wurde durchgeführt")
        #daten aus form auslesen
        #neuer title -> editItemFormObject.title.data
        #daten mit update in DB speichern

        itemId = editItemFormObject.itemId.data

        item_to_edit = db.session.query(Faecher).filter(Faecher.Faecher_Id == itemId).first()
        item_to_edit.Bzeichnung = editItemFormObject.Bzeichnung.data
        item_to_edit.Farbe = editItemFormObject.Farbe.data
        item_to_edit.describtion = editItemFormObject.describtion.data
        item_to_edit.Lehrraum = editItemFormObject.Lehrraum.data


        db.session.commit()

        return redirect("/")
    else:
        raise ("Fatal Error")