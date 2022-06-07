from flask import Flask, request, redirect, flash
from flask.templating import render_template
from flask import Blueprint
import sqlalchemy
from models import db, Lehrer
from forms.addLehrerForm import AddLehrerForm
from forms.deleteLehrerForm import DeleteLehrerForm
from forms.editLehrerForm import EditLehrerForm

lehrer_blueprint = Blueprint('lehrer_blueprint', __name__)


@lehrer_blueprint.route("/lehrer")
def lehrerLoad():

    page = request.args.get('page', 1, type=int)
    #session : sqlalchemy.orm.Session = db.session
    # schools = session.query(School).
    session: sqlalchemy.orm.scoping.scoped_session = db.session
    lehrer = session.query(Lehrer).order_by(
        Lehrer.Lehrer_Id).paginate(page, 5, error_out=False)

    return render_template('lehrerHTML/lehrer.html', paginator=lehrer)


@lehrer_blueprint.route("/lehrer/add", methods=["GET", "POST"])
def addLehrerForm():
    session: sqlalchemy.orm.scoping.scoped_session = db.session
    teacher = session.query(Lehrer).order_by(Lehrer.Lehrer_Id).all()

    adDTeacherForm = AddLehrerForm()

    if request.method == 'POST':

        if adDTeacherForm.validate_on_submit():
            print("gültig")

            # post kam zurück und ist valide

            print(adDTeacherForm.Vorname.data)
            print(adDTeacherForm.Nachname.data)
            print(adDTeacherForm.Faecher_Unterrichtet.data)
            print(adDTeacherForm.Anzahl_Klassen.data)
            # hier in DB Speichern

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
        return render_template("lehrerHTML/lehrer_add.html", Lehrer=Lehrer, form=adDTeacherForm)


@lehrer_blueprint.route("/lehrer/delete", methods=["post"])
def deleteLehrer():
    deleteLehrerformObj = DeleteLehrerForm()
    if deleteLehrerformObj.validate_on_submit():
        print("gültig")
        # db objekt holen
        # delete command ausführen

        itemIdToDelete = deleteLehrerformObj.Lehrer_Id.data
        itemToDelete = db.session.query(Lehrer).filter(
            Lehrer.Lehrer_Id == itemIdToDelete)
        itemToDelete.delete()

        db.session.commit()
    else:
        print("Fatal Error")

    flash(f"Item with id {itemIdToDelete} has been deleted")

    return redirect("/lehrer")


@lehrer_blueprint.route("/lehrer/edit", methods=["post"])
def submitEditForm():
    editItemFormObject = EditLehrerForm()

    if editItemFormObject.validate_on_submit():
        print("Submit wurde durchgeführt")
        # daten aus form auslesen
        # neuer title -> editItemFormObject.title.data
        # daten mit update in DB speichern

        itemId = editItemFormObject.Lehrer_Id.data

        item_to_edit = db.session.query(Lehrer).filter(
            Lehrer.Lehrer_Id == itemId).first()
        item_to_edit.Vorname = editItemFormObject.Vorname.data
        item_to_edit.Nachname = editItemFormObject.Nachname.data
        item_to_edit.Faecher_Unterrichtet = editItemFormObject.Faecher_Unterrichtet.data
        item_to_edit.Anzahl_Klassen = editItemFormObject.Anzahl_Klassen.data

        db.session.commit()

        return redirect("/lehrer")
    else:
        raise ("Fatal Error")


@lehrer_blueprint.route("/lehrer/edit")
def showEditForm():
    # hier itemid auslesen (wie kann man bei flask einen get parameter aus dem request auslesen)
    Lehrer_Id = request.args["Lehrer_Id"]

    # item laden (wie kann man einen datensatz lesen)
    item_to_edit = db.session.query(Lehrer).filter(
        Lehrer.Lehrer_Id == Lehrer_Id).first()

    editItemFormObject = EditLehrerForm()
    # form befüllen
    editItemFormObject.Lehrer_Id.data = item_to_edit.Lehrer_Id
    editItemFormObject.Vorname.data = item_to_edit.Vorname
    editItemFormObject.Nachname.data = item_to_edit.Nachname
    editItemFormObject.Faecher_Unterrichtet.data = item_to_edit.Faecher_Unterrichtet
    editItemFormObject.Anzahl_Klassen.data = item_to_edit.Anzahl_Klassen

    return render_template("lehrerHTML/lehrerEdit.html", form=editItemFormObject)
