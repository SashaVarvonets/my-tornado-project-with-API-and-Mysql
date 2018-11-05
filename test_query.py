import mysql.connector
from datetime import date, timedelta

class Test:
    def __init__(self, db, start_date=date.today()-timedelta(7), end_date=date.today()):
        self.db = db
        self.start_date = start_date
        self.end_date = end_date

    def make_query(self):
        my_cursor = self.db.cursor()
        print my_cursor
        my_cursor.execute("SELECT * from API_Data WHERE date BETWEEN %s and %s", (self.start_date, self.end_date))
        print(my_cursor)
        for x in my_cursor:
            print x


db = mysql.connector.connect(
        host="localhost",
        user="sasha",
        passwd="admin",
        database="imonomy_db"
    )




a = Test(db=db)
a.make_query()