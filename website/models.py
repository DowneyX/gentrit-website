from datetime import datetime
from flask_login import UserMixin
from . import db


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    uuid = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    first_name = db.Column(db.String(1000))
    last_name = db.Column(db.String(1000))
    phone_nr = db.Column(db.String(1000))
    role = db.Column(db.String(16), nullable=False, default='user')
    created_at = db.Column(db.Date(), nullable=False, default=datetime.now())
    updated_at = db.Column(db.Date(), nullable=True)
    deleted_at = db.Column(db.Date(), nullable=True)

    def get_id(self):
        return (self.uuid)
