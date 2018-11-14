from torndb_connector import DbConnector


def data_saver(data_list):
    connector = DbConnector()
    connector.create_db()

    for i in data_list:
        try:
            connector.add_values(i)
        except Exception as e:
            print e
    connector.show_all_values()
    return True

