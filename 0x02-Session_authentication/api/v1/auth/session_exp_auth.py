#!/usr/bin/env python3
"""SessionExpAuth class to expire a session"""
from api.v1.auth.session_auth import SessionAuth
from datetime import datetime, timedelta
from os import getenv


class SessionExpAuth(SessionAuth):
    """SessionExpAuth class"""
    def __init__(self):
        """Initialize class"""
        try:
            self.session_duration = int(getenv('SESSION_DURATION'))
        except Exception:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """Create session"""
        try:
            session_id = super().create_session(user_id)
        except Exception:
            return None
        session = {'user_id': user_id,
                   'created_at': datetime.now()}
        self.user_id_by_session_id[session_id] = session
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Return User ID based on Session ID"""
        if session_id is None or type(session_id) is not str:
            return None
        session = self.user_id_by_session_id.get(session_id)
        if session is None or 'created_at' not in session:
            return None

        if self.session_duration <= 0:
            return session.get('user_id')
        created_time = session.get('created_at')
        session_elapsed = timedelta(seconds=self.session_duration)
        if created_time + session_elapsed < datetime.now():
            return None
        else:
            return session.get('user_id')
