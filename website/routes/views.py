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


@views.route('/onze-diensten')
def our_services():
    return render_template('our_services.html')


@views.route('/over-ons')
def about_us():
    return render_template('about_us.html')


#################
# create routes #
#################


#################
# update routes #
#################


#################
# delete routes #
#################
