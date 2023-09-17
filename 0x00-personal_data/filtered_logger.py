#!/usr/bin/env python3
"""Personal data methods"""
from typing import List
import logging
import mysql.connector
import os
import re

PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


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


def get_logger() -> logging.Logger:
    """Return a Logger object"""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(PII_FIELDS)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Returns a connector to the db"""
    db_host = os.environ.get('PERSONAL_DATA_DB_HOST', 'localhost')
    db_user = os.environ.get('PERSONAL_DATA_DB_USERNAME', 'root')
    db_pass = os.environ.get('PERSONAL_DATA_DB_PASSWORD', '')
    db = os.environ.get('PERSONAL_DATA_DB_NAME')
    if not (db_host and db_user and db_pass and db):
        raise ValueError('Database credentials not found')
    try:
        conn = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_pass,
            database=db
        )
        return conn
    except mysql.connector.Error as err:
        print('Error: {}', err)
        return None


def main() -> None:
    """main function"""
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM users')
    logger = get_logger()
    fld_a = 'name={}; email={}; phone={}; ssn={}; password={}; ip={};'
    fld_b = 'last_login={}; user_agent={};'
    for row in cursor:
        fields = (fld_a + fld_b).format(row[0], row[1], row[2], row[3],
                                        row[4], row[5], row[6], row[7])
        logger.info(fields)
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
