#!/usr/bin/env python3
"""Personal data methods"""
from typing import List
import logging
import re


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """Obfuscate specific fields that match '=' plus other chars and separator
    using re.sub()"""
    temp = message
    for field in fields:
        temp = re.sub(field + "=.*?" + separator, field + "=" + redaction +
                      separator, temp)
    return temp


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Initilaize class"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """filter values in incoming logs using filter_datum"""
        return filter_datum(self.fields, self.REDACTION,
                            super(RedactingFormatter, self).format(record),
                            self.SEPARATOR)
