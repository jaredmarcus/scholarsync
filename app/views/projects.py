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
    collaboration_projects = Collaborator.query.filter_by(user_id=user_id).join(Project).all()

    owned_projects_response = [
        {
            'id': project.id,
            'name': project.name,
            'description': project.description,
            'created_at': project.created_at.isoformat()
        }
        for project in owned_projects
    ]

    collaboration_projects_response = [
        {
            'id': collaboration.project.id,
            'name': collaboration.project.name,
            'description': collaboration.project.description,
            'created_at': collaboration.project.created_at.isoformat(),
            'permissions': collaboration.permissions
        }
        for collaboration in collaboration_projects
    ]

    return jsonify(
        owned_projects=owned_projects_response,
        collaboration_projects=collaboration_projects_response
    )

@bp.route('/projects/<int:project_id>', methods=['PUT'])
@jwt_required()
def update_project(project_id):
    user_id = get_jwt_identity()
    project = Project.query.get(project_id)
    if not project or project.owner_id != user_id:
        return jsonify(message="Unauthorized"), 403

    project.name = request.json.get('name', project.name)
    project.description = request.json.get('description', project.description)
    db.session.commit()
    return jsonify(message="Project updated")
