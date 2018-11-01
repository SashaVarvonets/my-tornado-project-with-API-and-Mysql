import mysql.connector
from datetime import date


def save_data(data_list):

    mydb = mysql.connector.connect(
        host="localhost",
        user="sasha",
        passwd="admin",
        database="imonomy_db"
    )

    mycursor = mydb.cursor()
    # mycursor.execute('DROP TABLE API_Data;')
    # return
    # Creating Table API_Data
    try:
        mycursor.execute(
            "CREATE TABLE API_Data ("
            "date DATE, client_name VARCHAR(255), responses INT,"
            "impressions INT, revenue FLOAT(10,4), date_updated DATE,"
            "date_created DATE, PRIMARY KEY (date));"
        )
    except Exception as e:
        print e

    for i in data_list:
        try:
            val = (i['date'], 'Sasha', i['responses'], i['impressions'], i['revenue'], date.today())
            sql = "INSERT INTO API_Data (date, client_name, responses, impressions, revenue, date_created)" \
                  "VALUES (%s, %s, %s, %s, %s, %s);"
            mycursor.execute(sql, val)

        except Exception as e:
            print e
            val = (i['responses'], i['impressions'], i['revenue'], date.today(), i['date'])
            sql = "UPDATE API_Data Set responses=%s, impressions=%s, revenue=%s, date_updated=%s WHERE date=%s;"
            mycursor.execute(sql, val)
        mydb.commit()


    mycursor.execute("SELECT * from API_Data;")
    for x in mycursor:
        print x

    return True
