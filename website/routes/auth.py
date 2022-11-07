# auth.py
from datetime import datetime
from flask import Blueprint, render_template, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from ..forms import Create_user_form, Login_user_form, Update_password_form, Update_user_form
from ..models import User
from .. import db

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    redirect(url_for('views.home'))

    # check if user is already logged in

    # form submited

    # check if user actually exists
    # take the user supplied password, hash it, and compare it to the hashed password in database
    # if user doesn't exist or password is wrong, reload the page

    # # if the above check passes, then we know the user has the right credentials

    # return render_template('auth/login.html', form=form)


@auth.route('/sign-up', methods=['GET', 'POST'])
def signup():

    redirect(url_for('views.home'))

    # check if user is already logged in

    # form submitted

    # check if email is already in our database

    # check if passwords match

    # insert form data

    # add to database

    # return render_template('auth/sign_up.html', form=form)


@login_required
@auth.route('/logout')
def logout():
    flash("Gebruiker uitgelogd")
    logout_user()
    # return redirect(url_for('views.home'))


@login_required
@auth.route('/account')
def account():
    # return render_template('auth/account.html', current_user=current_user)
    pass


@login_required
@auth.route('/password-update', methods=['GET', 'POST'])
def update_password():

    # form submited

    # check if passwords match

    # check if password is correct

    # insert data

    # add to database

    # return render_template('auth/password_update.html', form=form, current_user=current_user)
    pass


@login_required
@auth.route('/account-update', methods=['GET', 'POST'])
def update_account():

    # form submitted

    # check if email is already in our database

    # insert data

    # add to database

    # setting form values

    # return render_template('auth/account_update.html', form=form, current_user=current_user)
    pass
