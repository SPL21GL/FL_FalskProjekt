from flask import Flask, request, flash, redirect, session
from flask.templating import render_template
from flask import Blueprint
import sqlalchemy
from models import Lehrer, SchuleLehrer, db, School
from forms.addSchulForm import AddSchulForm
from forms.deleteSchulForm import DeleteSchulForm
from forms.editSchulForm import EditSchulForm
import sqlalchemy.orm

school_blueprint = Blueprint('school_blueprint', __name__)


@school_blueprint.route("/schule")
def schulenLoad():

    page = request.args.get('page', 1, type=int)
    #session : sqlalchemy.orm.Session = db.session
    # schools = session.query(School).
    session: sqlalchemy.orm.scoping.scoped_session = db.session
    schools = session.query(School).order_by(
        School.school_Id).paginate(page, 5, error_out=False)

    return render_template('schoolHTML/Schul.html', paginator=schools)


@school_blueprint.route("/school/add", methods=["GET", "POST"])
def schools_add():
    session: sqlalchemy.orm.scoping.scoped_session = db.session
    school = session.query(School).order_by(School.school_Id).all()

    adDSchulForm = AddSchulForm()

    if request.method == 'POST':

        if adDSchulForm.validate_on_submit():
            print("gültig")

            # post kam zurück und ist valide
            print(adDSchulForm.Adresse.data)
            print(adDSchulForm.Anzahl_Schueler.data)
            print(adDSchulForm.Name_Schule.data)
            print(adDSchulForm.Schulart.data)
            # hier in DB Speichern

            newItem = School()
            newItem.Adresse = adDSchulForm.Adresse.data
            newItem.Anzahl_Schueler = adDSchulForm.Anzahl_Schueler.data
            newItem.Name_Schule = adDSchulForm.Name_Schule.data
            newItem.Schulart = adDSchulForm.Schulart.data

            db.session.add(newItem)
            db.session.commit()
            return redirect("/schule")

        else:
            raise "Fatal"
    else:
        return render_template("schoolHTML/schul_add.html", school=school, form=adDSchulForm)


# delete

@school_blueprint.route("/schul/delete", methods=["post"])
def deleteSchul():
    deleteSchulformObj = DeleteSchulForm()
    if deleteSchulformObj.validate_on_submit():
        print("gültig")
        # db objekt holen
        # delete command ausführen

        itemIdToDelete = deleteSchulformObj.school_Id.data
        itemToDelete = db.session.query(School).filter(
            School.school_Id == itemIdToDelete)
        itemToDelete.delete()

        db.session.commit()
    else:
        print("Fatal Error")

    flash(f"Item with id {itemIdToDelete} has been deleted")

    return redirect("/schule")


@school_blueprint.route("/schul/edit", methods=["post"])
def submitEditForm():
    editItemFormObject = EditSchulForm()

    if editItemFormObject.validate_on_submit():
        print("Submit wurde durchgeführt")
        # daten aus form auslesen
        # neuer title -> editItemFormObject.title.data
        # daten mit update in DB speichern

        itemId = editItemFormObject.school_Id.data

    if editItemFormObject.validate_on_submit():
        print("Submit wurde durchgeführt")
        # daten aus form auslesen
        # neuer title -> editItemFormObject.title.data
        # daten mit update in DB speichern

        itemId = editItemFormObject.school_Id.data

        item_to_edit = db.session.query(School).filter(
            School.school_Id == itemId).first()
        item_to_edit.Adresse = editItemFormObject.Adresse.data
        item_to_edit.Anzahl_Schueler = editItemFormObject.Anzahl_Schueler.data
        item_to_edit.Name_Schule = editItemFormObject.Name_Schule.data
        item_to_edit.Schulart = editItemFormObject.Schulart.data

        db.session.commit()

        return redirect("/schule")
    else:
        raise ("Fatal Error")


@school_blueprint.route("/schul/edit")
def showEditForm():
    # hier itemid auslesen (wie kann man bei flask einen get parameter aus dem request auslesen)
    school_Id = request.args["school_Id"]

    # item laden (wie kann man einen datensatz lesen)
    item_to_edit = db.session.query(School).filter(
        School.school_Id == school_Id).first()

    editItemFormObject = EditSchulForm()
    # form befüllen
    editItemFormObject.school_Id.data = item_to_edit.school_Id
    editItemFormObject.Adresse.data = item_to_edit.Adresse
    editItemFormObject.Anzahl_Schueler.data = item_to_edit.Anzahl_Schueler
    editItemFormObject.Name_Schule.data = item_to_edit.Name_Schule
    editItemFormObject.Schulart.data = item_to_edit.Schulart

    return render_template("schoolHTML/schulEdit.html", form=editItemFormObject)


#
# @school_blueprint.route('/schule')

# def schulenPaging():
 #   # Set the pagination configuration
  #  page = request.args.get('page', 1, type=int)
#
 #   schulen = School.query.paginate(page=page, per_page=ROWS_PER_PAGE)
  #  print(schulen)
   # return render_template('schoolHTML/Schul.html', schulen=schulen)
