from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.models.user import User
from app import db

auth_blueprint = Blueprint('auth', __name__, url_prefix='/auth')

@auth_blueprint.route('/login', methods=['GET'])
def login():
    return render_template('security/login.html')

@auth_blueprint.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    confirm_password = request.form['confirm_password']

    # Check if passwords match
    if password == confirm_password:
        # Save user credentials to database
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        
        # Redirect to login as registration is successful
        return redirect(url_for('auth.login'))
    else:
        flash('Passwords do not match!', 'error')
        return redirect(url_for('auth.register'))

@auth_blueprint.route('/logout')
def logout():
    session.pop('token', None)
    return redirect('/')