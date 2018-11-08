from datetime import date
from torndb_conector import my_db


def data_saver(data_list):
    today = date.today()

    try:
        my_db.query("CREATE TABLE API_Data_torndb ("
                    "date DATE, client_name VARCHAR(255), responses INT, impressions INT, revenue FLOAT(10,4),"
                    " date_updated DATE,date_created DATE, PRIMARY KEY (date));")
    except:
        pass

    for i in data_list:
        try:
            value = (i['date'], 'Sasha', i['responses'], i['impressions'], i['revenue'], today)

            my_db.execute("INSERT INTO API_Data_torndb ("
                          "date, client_name, responses, impressions, revenue, date_created)"
                          "VALUES (%s, %s, %s, %s, %s, %s);", *value)
        except Exception as e:
            # print e
            value = (i['responses'], i['impressions'], i['revenue'], today, i['date'])
            my_db.execute("UPDATE API_Data_torndb Set responses=%s, impressions=%s, revenue=%s, date_updated=%s"
                          " WHERE date=%s;",
                          *value)
    # for i in my_db.query("SELECT * from API_Data_torndb;"):
    #     print i

    return True

