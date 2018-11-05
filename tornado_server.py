import tornado.ioloop
import tornado.web
import mysql.connector
from datetime import date, timedelta


class DefaultDataHandler(tornado.web.RequestHandler):
    def initialize(self, db):
        self.db = db

    def get(self):
        try:
            start_date = self.get_argument("start_date", None)
        except: pass
        try:
            end_date = self.get_argument("end_date", None)
        except: pass

        if not start_date:
            start_date = date.today()-timedelta(7)
        if not end_date:
            end_date = date.today()

        cursor = self.db.cursor()
        cursor.execute("SELECT date, client_name, responses, impressions, revenue"
                       " from API_Data WHERE date BETWEEN %s and %s", (start_date, end_date))

        items = []

        # I don't know what i have to send for Jinja
        for i in cursor:
            lst = [i[0], i[1], i[2], i[3], i[4]]
            items.append(lst)

        self.render("template.html", items=items, start_date=start_date, end_date=end_date)


if __name__ == "__main__":
    db = mysql.connector.connect(
        host="localhost",
        user="sasha",
        passwd="admin",
        database="imonomy_db"
    )
    
    application = tornado.web.Application([
        (r"/", DefaultDataHandler, dict(db=db))
    ])
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
