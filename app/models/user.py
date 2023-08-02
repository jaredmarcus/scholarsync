from app import db
from flask_security.models import fsqla_v3 as fsqla

class User(db.Model, fsqla.FsUserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    roles = db.relationship('Role', secondary='user_roles')
