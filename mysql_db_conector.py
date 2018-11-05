import mysql.connector

host="localhost"
user="root"
password="root"
database="imonomy_db"


db = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database,
)