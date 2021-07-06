from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, IntegerField, DateField, SelectField, HiddenField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError,Regexp
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from laud import db
from laud.models import Metadata
from wtforms.fields.html5 import DateField

species = Metadata.query.with_entities(Metadata.taxa_name).distinct()
subject_id = Metadata.query.with_entities(Metadata.subject_id).distinct()

# test choices (select field)
species1=list()
for row in species:
    rowDict=row._asdict()
    species1.append(rowDict)
species_choice = [(row['taxa_name'],row['taxa_name']) for row in species1]

subject_id1 = list()
for row in subject_id:
    rowDict=row._asdict()
    subject_id1.append(rowDict)
subject_choice = [(row['subject_id'],row['subject_id']) for row in subject_id1]

class ChoiceForm(FlaskForm):
    species_result=SelectField('Species Choice', choices=species_choice)
    subject_result=SelectField('Sample ID Choice', choices=subject_choice)
    submit = SubmitField('Submit')
