from flask_wtf import FlaskForm
from wtforms import ValidationError
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.fields import (
    PasswordField,
    StringField,
    SubmitField,
    IntegerField
)
from wtforms.fields.html5 import EmailField
from wtforms.validators import (
    Email,
    EqualTo,
    InputRequired,
    Length,
    NumberRange
)

from app import db
from app.models import Vereniging

class AddBeerForm(FlaskForm):
    vereniging = QuerySelectField('Vereniging', validators=[InputRequired()], get_label='name',
                            query_factory=lambda: db.session.query(Vereniging).order_by('name'))
    amount = IntegerField('Aantal munten', validators=[InputRequired(), NumberRange(min=0)])
    
    submit = SubmitField('Toevoegen')

class NewForm(FlaskForm):
    naam = StringField('Naam', validators=[InputRequired()])
    aantal = IntegerField('Aantal munten gekocht', validators=[InputRequired(), NumberRange(min=0)])
    submit = SubmitField('Toevoegen')
