from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email

class ContactForm(FlaskForm):
    firstname = StringField('First Name',
            validators=[DataRequired(), Length(min=1, max=20)])
    lastname = StringField('Last Name',
            validators=[DataRequired(), Length(min=1, max=20)])
    email = StringField('Email',
            validators=[DataRequired(), Email()])
    subscribe = BooleanField('Subscribe to Newsletter')
    user_input = StringField('Question or Comment',
            validators=[Length(min=0, max=500)])
    submit = SubmitField('Submit')