import mysql.connector, os
from os import environ
from mysql.connector import connect 

def returnConnection():
    conn = connect(
        host = environ.get('DB_URL'),
        user = environ.get('DB_USER'),
        password = environ.get('DB_PASSWORD'),
        database = environ.get('DB_NAME')
    )
    return conn

