import sqlalchemy
import sqlalchemy.orm

from flask import redirect, request, flash
from flask.templating import render_template
from flask import Blueprint
from forms.Schule_Lehrer_delete import OrderdetailDeleteForm
from forms.schule_lehrer import OrderdetailForm
from models import SchuleLehrer, Lehrer, db


orderdetails_blueprint = Blueprint('orderdetails_blueprint', __name__)

@orderdetails_blueprint.route("/schule_lehrer/add", methods=["GET", "POST"])
def add_teacher():
    school_Id = int(request.args["school_Id"])
    session: sqlalchemy.orm.scoping.scoped_session = db.session
    add_order_form = OrderdetailForm()

    session.query(Lehrer).order_by(Lehrer.Lehrer_Id).all()

    lehrer = session.query(Lehrer).order_by(Lehrer.Lehrer_Id).all()

    product_list = [(str(p.Lehrer_Id), p.Vorname)
                for p in Lehrer]

    Lehrer.Lehrer_Id.choices = [(c.Lehrer_Id, c.Nachname) for c in session.query(Lehrer).order_by(Lehrer.Lehrer_Id).all()
]   
    add_order_form.Lehrer_Id.choices = product_list

    return redirect('schuleLehrer/schuleLehreradd.html')



# @orderdetails_blueprint.route("/orderdetails/delete", methods=["post"])
# def deleteorder():
#     delete_item_form_obj = OrderdetailDeleteForm()
#     if delete_item_form_obj.validate_on_submit():

#         order_number_to_delete = int(delete_item_form_obj.Lehrer_Id.data)
#         product_code_to_delete = (delete_item_form_obj.productCode.data)
#         orderdetail_to_delete = db.session.query(SchuleLehrer).filter(
#             sqlalchemy.and_(
#                 SchuleLehrer.Nachname == order_number_to_delete,

#         ))
#         orderdetail_to_delete.delete()

#         db.session.commit()
#     else:
#         print("Fatal Error")

#     flash(f"Product with id {product_code_to_delete} has been deleted")

#     return redirect("/lehrer/edit?Lehrer_Id=" + str(order_number_to_delete))

