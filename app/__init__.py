from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore

db = SQLAlchemy()
security = Security()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config')

    db.init_app(app)
    from .models.user import User
    from .models.role import Role
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security.init_app(app, user_datastore)

    from .views.auth import auth_blueprint
    app.register_blueprint(auth_blueprint)

    @app.before_first_request
    def create_tables():
        db.create_all()

    return app
