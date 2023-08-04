from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore

db = SQLAlchemy()
security = Security()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config')

    db.init_app(app)

    from app.models import user, role
    user_datastore = SQLAlchemyUserDatastore(db, user.User, role.Role)
    security.init_app(app, user_datastore)

    from app.views import auth_blueprint, projects
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(projects.bp, url_prefix='/projects')

    with app.app_context():
        db.create_all()

    return app
