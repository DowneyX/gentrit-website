from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = 'database.db'


def create_app():
    """ initialises the website"""

    app = Flask(__name__, template_folder='templates')

    login_manager = LoginManager()
    login_manager.init_app(app)

    # WHEN IN PRODUCTION NEVER SHARE THIS KEY AND CHANGE IT TO SOMETHING THAT MAKES MORE SENSE LIKE A HASH
    app.config['SECRET_KEY'] = 'ThisIsSecret'
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_NAME}"
    db.init_app(app)
    # db.create_all(app=app)

    from .routes.views import views
    #from .routes.auth import auth

    app.register_blueprint(views, url_prefix='/')
    #app.register_blueprint(auth, url_prefix='/auth')

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app
