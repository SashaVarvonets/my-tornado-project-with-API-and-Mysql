import mysql.connector

host="localhost"
user="sasha"
password="admin"
database="imonomy_db"


db = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database,
)