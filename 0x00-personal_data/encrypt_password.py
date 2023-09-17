#!/usr/bin/env python3
"""Encrypt user passwords"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Return a hashed password"""
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password
