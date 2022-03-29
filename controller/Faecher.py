from flask import Flask,request,redirect,flash
from flask.templating import render_template
from flask import Blueprint
import sqlalchemy
from models import Faecher, db,School
from forms.addFaecherForm import AddFaecherForm
from forms.deleteFachForm import DeleteFaecherForm
from forms.editFaecherFrom import EditFaecherForm


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

        itemId = editItemFormObject.Faecher_Id.data

        item_to_edit = db.session.query(Faecher).filter(Faecher.Faecher_Id == itemId).first()
        item_to_edit.Bzeichnung = editItemFormObject.Bzeichnung.data
        item_to_edit.Farbe = editItemFormObject.Farbe.data
        item_to_edit.description = editItemFormObject.description.data
        item_to_edit.Lehrraum = editItemFormObject.Lehrraum.data


        db.session.commit()

        return redirect("/faecher")
    else:
        raise ("Fatal Error")


@faecher_blueprint.route("/faecher/edit")
def showEditForm():
    #hier itemid auslesen (wie kann man bei flask einen get parameter aus dem request auslesen)
    Faecher_Id = request.args["Faecher_Id"]

    #item laden (wie kann man einen datensatz lesen)
    item_to_edit = db.session.query(Faecher).filter(Faecher.Faecher_Id == Faecher_Id).first()
    
    editItemFormObject = EditFaecherForm()
    #form befüllen
    editItemFormObject.Faecher_Id.data = item_to_edit.Faecher_Id
    editItemFormObject.Bzeichnung.data = item_to_edit.Bzeichnung
    editItemFormObject.Farbe.data = item_to_edit.Farbe
    editItemFormObject.description.data = item_to_edit.description
    editItemFormObject.Lehrraum.data = item_to_edit.Lehrraum
    
    
    return render_template("faecherHTML/faecherEdit.html", form = editItemFormObject)

