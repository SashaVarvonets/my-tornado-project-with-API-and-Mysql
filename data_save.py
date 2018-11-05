
from datetime import date


def save_data(data_list, my_db):
    my_cursor = my_db.cursor()
    # my_cursor.execute('DROP TABLE API_Data;')
    # return
    # Creating Table API_Data
    try:
        my_cursor.execute(
            "CREATE TABLE API_Data ("
            "date DATE, client_name VARCHAR(255), responses INT,"
            "impressions INT, revenue FLOAT(10,4), date_updated DATE,"
            "date_created DATE, PRIMARY KEY (date));"
        )
    except:
        pass

    for i in data_list:
        try:
            val = (i['date'], 'Sasha', i['responses'], i['impressions'], i['revenue'], date.today())
            sql = "INSERT INTO API_Data (date, client_name, responses, impressions, revenue, date_created)" \
                  "VALUES (%s, %s, %s, %s, %s, %s);"
            my_cursor.execute(sql, val)

        except:
            val = (i['responses'], i['impressions'], i['revenue'], date.today(), i['date'])
            sql = "UPDATE API_Data Set responses=%s, impressions=%s, revenue=%s, date_updated=%s WHERE date=%s;"
            my_cursor.execute(sql, val)
        my_db.commit()

    # my_cursor.execute("SELECT * from API_Data;")
    # for x in my_cursor:
    #     print x

    return True
