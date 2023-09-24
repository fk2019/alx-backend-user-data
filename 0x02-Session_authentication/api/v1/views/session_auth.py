#!/usr/bin/env python3
""" Module of session_auth views
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def view_session() -> str:
    """ POST /api/v1/auth_session/login
    Return:
      - handle route for session authentication
    """
    email = request.form.get('email')
    password = request.form.get('password')
    if not email or email == '':
        return jsonify({'error': 'email missing'}), 400
    if not password or password == '':
        return jsonify({'error': 'password missing'}), 400
    try:
        users = User.search({'email': email})
    except Exception:
        return jsonify({'error': 'no user found for this email'}), 404
    if not users:
        return jsonify({'error': 'no user found for this email'}), 404
    user = users[0]
    if not user.is_valid_password(password):
        return jsonify({'error': 'wrong password'}), 401
    from api.v1.app import auth
    session_cookie = getenv('SESSION_NAME')
    session_id = auth.create_session(user.id)
    res = jsonify(user.to_json())
    res.set_cookie(session_cookie, session_id)
    return res
