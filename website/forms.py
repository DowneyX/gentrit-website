from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, FloatField, RadioField, TextAreaField, SubmitField,DateField, EmailField, PasswordField,)
from wtforms.validators import DataRequired, Email, Length, ValidationError

class Create_user_form(FlaskForm):
    first_name = StringField("Voornaam", validators=[DataRequired(), Length(2,1000)])
    last_name = StringField("Achternaam", validators=[DataRequired(), Length(2,1000)])
    email = EmailField("E-mail", validators=[DataRequired(), Email(),Length(3,50)])
    phone_nr = StringField("Telefoon", validators=[DataRequired(), Length(0,16)])
    password1 = PasswordField("Wachtwoord", validators=[DataRequired(), Length(2,100)])
    password2 = PasswordField("Wachtwoord opnieuw", validators=[DataRequired(), Length(2,100)])
    submit = SubmitField("Registreer") 

    def validate_phone_nr(form, field):
        if not field.data.isdigit():
            raise ValidationError("is niet een nummer")

class Update_password_form(FlaskForm):
    current_password = PasswordField("Huidige wachtwoord", validators=[DataRequired(), Length(2,100)])
    password1 = PasswordField("Nieuwe wachtwoord", validators=[DataRequired(), Length(2,100)])
    password2 = PasswordField("Nieuwe wachtwoord opnieuw", validators=[DataRequired(), Length(2,100)])
    submit = SubmitField("Update") 

class Update_user_form(FlaskForm):
    first_name = StringField("Voornaam", validators=[DataRequired(), Length(2,1000)])
    last_name = StringField("Achternaam", validators=[DataRequired(), Length(2,1000)])
    email = EmailField("E-mail", validators=[DataRequired(), Email(),Length(3,50)])
    phone_nr = StringField("Telefoon", validators=[DataRequired(), Length(1,16)])
    submit = SubmitField("Update")

    def validate_phone_nr(form, field):
        if not field.data.isdigit():
            raise ValidationError("is niet een nummer")

class Update_user_role_form(FlaskForm):
    role = RadioField('welke rol dien je aan deze gebruiker toe', choices=[('admin','administrator'),('user','gebruiker')], validators=[DataRequired()])
    submit = SubmitField("Update")

class Login_user_form(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired()])
    password = PasswordField("Wachtwoord", validators=[DataRequired()])
    remember = BooleanField("Onthoud mij")
    submit = SubmitField("Login")

