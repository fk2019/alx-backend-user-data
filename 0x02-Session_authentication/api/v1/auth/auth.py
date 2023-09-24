#!/usr/bin/env python3
"""Authentication class"""
from flask import request
from typing import List, TypeVar
from os import getenv


class Auth:
    """Auth class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Return False if path present in excluded paths else True"""
        if path is None or excluded_paths == []:
            return True
        if (path + '/') in excluded_paths:
            return False
        for ex_path in excluded_paths:
            if ex_path in {path, path + '/'}:
                return False
            elif ex_path.endswith('*') and path.startswith(ex_path[:-1]):
                return False
            else:
                return True

    def authorization_header(self, request=None) -> str:
        """Return None"""
        if request is None:
            return None
        if 'Authorization' not in request.headers:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """Return None"""

    def session_cookie(self, request=None) -> str:
        """Return cookie value from request"""
        if request is None:
            return None
        session_name = getenv('SESSION_NAME')
        return request.cookies.get(session_name)
