from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, FloatField, RadioField,
                     TextAreaField, SubmitField, DateField, EmailField, PasswordField,)
from wtforms.validators import DataRequired, Email, Length, ValidationError


class contact_form(FlaskForm):
    full_name = StringField("Voornaam", validators=[
        DataRequired(), Length(2, 1000)])

    email = EmailField(
        "E-mail", validators=[DataRequired(), Email(), Length(3, 50)])
    phone_nr = StringField("Telefoon", validators=[
                           DataRequired(), Length(0, 16)])
    submit = SubmitField("verzend!")

    def validate_phone_nr(form, field):
        if not field.data.isdigit():
            raise ValidationError("is niet een nummer")
