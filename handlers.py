from datetime import date, timedelta
import tornado.web


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

        items = [[j for j in i] for i in cursor]

        self.render("template.html", items=items, start_date=start_date, end_date=end_date)