from app import db
from flask_security.models import fsqla_v3 as fsqla

class Role(db.Model, fsqla.FsRoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))
