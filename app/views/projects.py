from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.user import User
from app.models.project import Project, Collaborator, db

bp = Blueprint('projects', __name__)

@bp.route('/create', methods=['POST'])
@jwt_required()
def create_project():
    user_id = get_jwt_identity()
    name = request.json.get('name')
    description = request.json.get('description')
    project = Project(name=name, description=description, owner_id=user_id)
    db.session.add(project)
    db.session.commit()
    return jsonify(message="Project created"), 201

@bp.route('/invite', methods=['POST'])
@jwt_required()
def invite_collaborator():
    user_id = get_jwt_identity()
    project_id = request.json.get('project_id')
    collaborator_email = request.json.get('collaborator_email')
    permissions = request.json.get('permissions')

    project = Project.query.get(project_id)
    if not project or project.owner_id != user_id:
        return jsonify(message="Unauthorized"), 403

    collaborator_user = User.query.filter_by(email=collaborator_email).first()
    if not collaborator_user:
        return jsonify(message="User not found"), 404

    collaborator = Collaborator(user_id=collaborator_user.id, project_id=project_id, permissions=permissions)
    db.session.add(collaborator)
    db.session.commit()
    return jsonify(message="Collaborator invited")

@bp.route('/projects', methods=['GET'])
@jwt_required()
def list_projects():
    user_id = get_jwt_identity()
    owned_projects = Project.query.filter_by(owner_id=user_id).all()
    collaboration_projects = Collaborator.query.filter_by(user_id=user_id).all()
    # Convert projects to a suitable format for response
    # ...
    return jsonify(owned_projects=..., collaboration_projects=...)

# Additional endpoints can be added to manage project workflow, update projects, remove collaborators, etc.
