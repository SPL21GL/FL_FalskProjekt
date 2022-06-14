import sqlalchemy
import sqlalchemy.orm

from flask import redirect, request, flash
from flask.templating import render_template
from flask import Blueprint
from forms.Schule_Lehrer_delete import OrderdetailDeleteForm
from forms.schule_lehrer import OrderdetailForm
from models import SchuleLehrer, Lehrer, db


orderdetails_blueprint = Blueprint('orderdetails_blueprint', __name__)


@orderdetails_blueprint.route("/orderdetails/edit", methods=["GET", "POST"])
def orders_edit():
    session: sqlalchemy.orm.scoping.scoped_session = db.session

    order_detail_form = OrderdetailForm()
    products = session.query(Lehrer).order_by(Lehrer.Lehrer_Id).all()
    product_list = [(str(p.Lehrer_Id), p.Nachname)
                    for p in products]
    order_detail_form.Lehrer_Id.choices = product_list

    order_number = int(request.args["Lehrer_Id"])
    product_code = request.args["Lehrer_Id"]
    order_detail_form.Lehrer_Id.choices
    order_detail_query: sqlalchemy.orm.query.Query = session.query(SchuleLehrer)
    order_detail_to_edit: SchuleLehrer = order_detail_query.filter(
        sqlalchemy.and_(
            SchuleLehrer.Nachname == order_number))

    if request.method == "POST":
        if order_detail_form.validate_on_submit():

            order_detail_to_edit.Nachname = order_detail_form.Nachname.data

            db.session.commit()
            return redirect("/lehrer/edit?Lehrer_Id=" + str(order_number))

    else:
        order_detail_form.Nachname.data = order_detail_to_edit.Nachname

        return render_template("schuleLehrer/schuleLehrerEdit.html", form=order_detail_form)


@orderdetails_blueprint.route("/orderdetails/delete", methods=["post"])
def deleteorder():
    delete_item_form_obj = OrderdetailDeleteForm()
    if delete_item_form_obj.validate_on_submit():

        order_number_to_delete = int(delete_item_form_obj.Lehrer_Id.data)
        product_code_to_delete = (delete_item_form_obj.productCode.data)
        orderdetail_to_delete = db.session.query(SchuleLehrer).filter(
            sqlalchemy.and_(
                SchuleLehrer.Nachname == order_number_to_delete,

        ))
        orderdetail_to_delete.delete()

        db.session.commit()
    else:
        print("Fatal Error")

    flash(f"Product with id {product_code_to_delete} has been deleted")

    return redirect("/lehrer/edit?Lehrer_Id=" + str(order_number_to_delete))

