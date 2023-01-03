from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,BooleanField,SelectField,RadioField
from wtforms.validators import Optional,InputRequired,URL,NumberRange

# species=['cat','dog','porcupine']

class AddPetForm(FlaskForm):
    """form for adding pets"""
    name = StringField('Pet name')
    species = SelectField('Species',choices=['cat','dog','porcupine'])
    photo_url = StringField("Photo_URL",validators=[Optional(), URL()])
    age = IntegerField('age',validators=[Optional(), NumberRange(min=0, max= 30)])
    is_available = BooleanField("available")
    Notes = StringField('Notes')