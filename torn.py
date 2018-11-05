import tornado.ioloop
import tornado.web
import mysql.connector
from datetime import date, timedelta


class DefaultDataHandler(tornado.web.RequestHandler):
    def initialize(self, db, start_date=date.today()-timedelta(7), end_date=date.today()):
        self.db = db
        self.start_date = start_date
        self.end_date = end_date

    def get(self):
        cursor = self.db.cursor()
        cursor.execute("SELECT * from API_Data WHERE date BETWEEN %s and %s", (self.start_date, self.end_date))
        
        for x in cursor:
            print x
        
        self.render("template.txt", items=cursor)


if __name__ == "__main__":
    db = mysql.connector.connect(
        host="localhost",
        user="sasha",
        passwd="admin",
        database="imonomy_db"
    )
    
    application = tornado.web.Application([
        (r"/", DefaultDataHandler, dict(db=db, start_date=date.today(), end_date=date.today()-timedelta(7))),
    ])
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
