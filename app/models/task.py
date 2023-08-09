from datetime import datetime
from app.models.user import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    deadline = db.Column(db.DateTime)
    status = db.Column(db.String(50), default="Not Started")  # Could also use an Enum type for better validation
    priority = db.Column(db.String(50), default="Medium")    # Could also use an Enum type for this
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)
    assignee_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # Foreign Key referencing User model
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))  # Foreign Key referencing Project model

    assignee = db.relationship('User', backref='tasks')
    project = db.relationship('Project', backref='tasks')
