import mysql.connector

USER_NAME = 'root'
PASSWORD = "root"
DATE_BASE_NAME = 'analytic_data_store'


def insert(query):
    """
    Метод подключается к БД и делает insert
    :param query: insert query
    :return: null
    """
    cnx = mysql.connector.connect(user=USER_NAME, database=DATE_BASE_NAME, password=PASSWORD)
    cursor = cnx.cursor()

    try:
        cursor.execute(query)
        # Make sure data is committed to the database
        cnx.commit()
    except Exception as mysql_error:
        print(query)
        print(mysql_error)
    finally:
        cursor.close()
        cnx.close()


def get_events_from_db():
    game_query = "SELECT id, key_event, json_data, user_secret_key, level_session_id, event_datetime " \
                 "FROM analytic_data_store.tester_data"

    cnx = mysql.connector.connect(user=USER_NAME, database=DATE_BASE_NAME, password=PASSWORD)
    cursor = cnx.cursor()

    events = dict()
    try:
        cursor.execute(game_query)
        for id, key_event, json_data, user_secret_key, level_session_id, event_datetime in cursor:
            events[id] = {"json_data": json_data, "user_secret_key": user_secret_key, "key_event": key_event,
                          "level_session_id": level_session_id, "event_datetime": event_datetime}
    except Exception as mysql_error:
        print(mysql_error)
    finally:
        cursor.close()
        cnx.close()
        return events
