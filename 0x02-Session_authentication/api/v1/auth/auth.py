#!/usr/bin/env python3
"""Authentication class"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Auth class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Return False if path present in excluded paths else True"""
        if path is None or excluded_paths == []:
            return True
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
