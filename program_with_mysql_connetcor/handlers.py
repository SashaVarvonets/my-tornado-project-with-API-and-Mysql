from datetime import date, timedelta
import tornado.web


class RowObject:
    def __init__(self, date, client_name, responses, impressions, revenue):
        self.date = date
        self.client_name = client_name
        self.responses = responses
        self.impressions = impressions
        self.revenue = revenue


class DefaultDataHandler(tornado.web.RequestHandler):
    def initialize(self, db):
        self.db = db

    def get(self):
        start_date = self.get_argument("start_date", None)
        end_date = self.get_argument("end_date", None)

        if not start_date:
            start_date = date.today()-timedelta(6)
        if not end_date:
            end_date = date.today()

        cursor = self.db.cursor()
        query = "SELECT date, client_name, responses, impressions, revenue FROM API_Data WHERE date BETWEEN %s AND %s"
        cursor.execute(query, (start_date, end_date))
        my_result = cursor.fetchall()

        items = []
        # if need make a list of objects
        for row in my_result:
            a = RowObject(*row)
            items.append(a)

        # if need make a list of lists
        # items = [[j for j in i] for i in my_result]

        self.render("template.html", items=items, start_date=start_date, end_date=end_date)
