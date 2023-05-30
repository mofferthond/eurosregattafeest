from flask import Blueprint, render_template, flash, redirect, url_for

from app import db
from app.models import EditableHTML
from .forms import AddBeerForm, NewForm
from app.models import Vereniging

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('main/index.html')

@main.route('/data')
def data():
    verenigingen = Vereniging.query.order_by(Vereniging.beer_count.desc()).all()
    json = {
        "data": []
        }
    for v in verenigingen:
        json["data"].append({
            "id": v.id,
            "naam": v.name,
            "total": v.beer_count
            })
    return json



@main.route('/new', methods=["GET", "POST"])
def new():
    form = NewForm()
    if form.validate_on_submit():
        vereniging = Vereniging(form.naam.data)
        vereniging.add_beer(form.aantal.data)
        db.session.add(vereniging)
        db.session.commit()

    return render_template('main/new.html', form=form)




@main.route('/admin', methods=["GET", "POST"])
def admin():
    form = AddBeerForm()
    if form.validate_on_submit():

        vereniging = Vereniging.query.filter_by(id=form.vereniging.data.id).first()
        amount = form.amount.data
        vereniging.add_beer(amount)

        db.session.add(vereniging)
        db.session.commit()
        flash("Vereniging " + vereniging.name + " is geupdate met +" + str(form.amount.data)  + " bier", "success")
        return redirect(url_for('main.admin'))
    return render_template('main/admin.html', form=form)
