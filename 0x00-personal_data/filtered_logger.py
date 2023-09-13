#!/usr/bin/env python3
"""Personal data methods"""
import re


def filter_datum(fields: list, redaction: str, message: str,
                 separator: str) -> str:
    """Obfuscate specific fields that match '=' plus other chars and separator
    using re.sub()"""
    temp = message
    for field in fields:
        temp = re.sub(field + "=.*?" + separator, field + "=" + redaction +
                      separator, temp)
    return temp
