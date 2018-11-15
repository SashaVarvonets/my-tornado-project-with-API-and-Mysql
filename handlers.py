from datetime import date, timedelta

import tornado.web


class DefaultDataHandler(tornado.web.RequestHandler):
    def initialize(self, db):
        self.db = db

    def get(self):
        start_date_error, end_date_error = '', ''
        start_date = date.today() - timedelta(6)
        end_date = date.today()

        # checking if the GET request has arguments
        if self.request.arguments:
            # Get arguments
            start_date = self.get_argument("start_date", None)
            end_date = self.get_argument("end_date", None)

            # Checking if start_date is correct
            try:
                start_date = date.strftime(date(*[int(i)for i in start_date.split('-')]), "%Y-%m-%d")
            except Exception as e:
                print start_date, e
                start_date_error = 'Write correct start date like "2000-12-01"'

            # Checking if end_date is correct
            try:
                end_date = date.strftime(date(*[int(i)for i in end_date.split('-')]), "%Y-%m-%d")
            except Exception as e:
                print end_date, e
                end_date_error = 'Write correct end date like "2000-12-01"'

        items = self.db.get_values_between_dates(start_date, end_date)

        self.render("template.html", items=items, start_date=start_date, end_date=end_date,
                    start_date_error=start_date_error, end_date_error=end_date_error)
