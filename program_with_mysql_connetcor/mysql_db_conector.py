import mysql.connector

host = "localhost"
user = "sasha"
password = "admin"
database = "imonomy_db"

try:
    my_db = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database,
    )
except Exception as e:
    print e
