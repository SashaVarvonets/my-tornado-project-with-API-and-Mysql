import torndb
#
host = "localhost"
user = "user"
password = "1000g0001"
database = "imonomy_db"


class DbConnector(object):
    def __init__(self):
        self.params = {
            'host': host,
            'user': user,
            'password': password,
            'database': database,
        }
        self.connector = torndb.Connection(**self.params)

    def show_all_values(self):
        for i in self.connector.query("SELECT * from API_Data_torndb;"):
            print i

    def get_values_between_dates(self, start_date, end_date):
        res = self.connector.query("""SELECT date, name, responses, impressions, revenue FROM API_Data_torndb
                                        WHERE date BETWEEN %s AND %s""", start_date, end_date)
        return res

    def create_db(self):
        try:
            self.connector.execute("""CREATE TABLE API_Data_torndb (
                                      date DATE,
                                      name VARCHAR(255),
                                      responses INT,
                                      impressions INT, 
                                      revenue FLOAT(10,4), 
                                      date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                                      date_updated TIMESTAMP NULL ON UPDATE CURRENT_TIMESTAMP,
                                      PRIMARY KEY (date, name));""")
            return True
        except Exception as e:
            print e

    def add_values(self, i):
        values = (i['date'], 'Sasha', i['responses'], i['impressions'], i['revenue'])
        self.connector.execute("""INSERT INTO API_Data_torndb (date, name, responses, impressions, revenue)
                                  VALUES (%s, %s, %s, %s, %s)
                                  ON DUPLICATE KEY UPDATE
                                  responses=VALUES(responses),
                                  impressions=VALUES(impressions),
                                  revenue=VALUES(revenue);""",
                               *values)
