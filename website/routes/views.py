from datetime import date, datetime
from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import current_user, login_required
from .. import db

views = Blueprint('views', __name__)

###############
# read routes #
###############


@views.route('/')
def home():
    return render_template('home.html')


@views.route('/contact')
def contact():
    return render_template('contact.html')


#################
# create routes #
#################


#################
# update routes #
#################


#################
# delete routes #
#################
