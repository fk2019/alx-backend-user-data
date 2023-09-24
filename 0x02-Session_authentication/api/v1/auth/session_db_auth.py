#!/usr/bin/env python3
"""SessionDBAuth class to authenticate DB"""
from api.v1.auth.session_exp_auth import SessionExpAuth
from os import getenv


class SessionDBAuth(SessionExpAuth):
    """SessionDBAuth class"""
    def create_session(self, user_id=None) -> str:
        """create session id"""
        return super().create_session(user_id)

    def user_id_for_session_id(self, session_id=None) -> str:
        """Return user id by requested user  session in db"""
        return super().user_id_for_session_id(session_id)

    def destroy_session(self, request=None):
        """delete user session based on request cookie"""
        return super().destrot_session(request)
