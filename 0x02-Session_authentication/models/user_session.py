#!/usr/bin/env python3
"""Database for storing session ids"""
from models.base import Base


class UserSession(Base):
    """User session model"""
    def __init__(self, *args: list, **kwargs: dict):
        """Initialize the class"""
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
