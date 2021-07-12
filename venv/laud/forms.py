from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, IntegerField, DateField, SelectField, HiddenField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError,Regexp
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from laud import db
from laud.models import Metadata
from wtforms.fields.html5 import DateField

sample_id = Metadata.query.with_entities(Metadata.sample_id).distinct()
subject_id = Metadata.query.with_entities(Metadata.subject_id).distinct()
event = Metadata.query.with_entities(Metadata.event).distinct()
taxa_type = Metadata.query.with_entities(Metadata.taxa_type).distinct()
species = Metadata.query.with_entities(Metadata.taxa_name).distinct()
cure = Metadata.query.with_entities(Metadata.cure_status).distinct()

# mysql query choices (select field)

# sample id
sample_id1 = list()
for row in sample_id:
    rowDict=row._asdict()
    sample_id1.append(rowDict)
sample_choice = [(row['sample_id'],row['sample_id']) for row in sample_id1]

# subject id
subject_id1 = list()
for row in subject_id:
    rowDict=row._asdict()
    subject_id1.append(rowDict)
subject_choice = [("%%","")]+[(row['subject_id'],row['subject_id']) for row in subject_id1]

# event
event1 = list()
for row in event:
    rowDict=row._asdict()
    event1.append(rowDict)
event_choice = [("%%","")]+[(row['event'],row['event']) for row in event1]

# taxa type
taxa_type1=list()
for row in taxa_type:
    rowDict=row._asdict()
    taxa_type1.append(rowDict)
type_choice = [(row['taxa_type'],row['taxa_type']) for row in taxa_type1]

# taxa name
species1=list()
for row in species:
    rowDict=row._asdict()
    species1.append(rowDict)
species_choice = [("%%","")]+[(row['taxa_name'],row['taxa_name']) for row in species1]

# cure status
cure1=list()
for row in cure:
    rowDict=row._asdict()
    cure1.append(rowDict)
cure_choice = [(row['cure_status'],row['cure_status']) for row in cure1]

class ChoiceForm(FlaskForm):
    #sample_result=SelectField('Sample ID', choices=sample_choice, default=None)
    subject_result=SelectField('Subject ID', choices=subject_choice, default=None)
    event_result=SelectField('Event', choices=event_choice, default=None)
    #type_result=SelectField('Taxa Type', choices=type_choice, default=None)
    species_result=SelectField('Species', choices=species_choice, default=None)
    #cure_result=SelectField('Cure Status', choices=cure_choice, default='')
    submit = SubmitField('Submit')

class _16SID(FlaskForm):
     FASTA_ID=StringField('BLAST hit:', validators=[DataRequired(),Length(max=100)])
     submit = SubmitField('Submit')
