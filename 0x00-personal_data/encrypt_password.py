#!/usr/bin/env python3
"""Encrypt user passwords"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Return a hashed password"""
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Validate user password"""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
