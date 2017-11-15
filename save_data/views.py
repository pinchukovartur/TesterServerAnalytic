from django.http import HttpResponse
import mysql.connector

# the method return user script
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import json


@csrf_exempt
def save_data(request):
    try:
        key = request.POST['key']
        data = request.POST['data']
        user_secret_key = request.POST['user_secret_key']
        level_session_id = request.POST['level_session_id']

        query = "INSERT INTO analytic_data_store.tesert_data (key_event, json_data, user_secret_key, level_session_id)" \
                " VALUES('" + key + "', '" + data + "', '" + user_secret_key + "', '" + level_session_id + "'); "
        __insert__(query)

    except Exception as error:
        print(error)
        return HttpResponse(str(error))

    return HttpResponse("200")


def index(request):
    return render(request, 'analytic_data/index.html')


def __insert__(query):
    """
    Метод подключается к БД и делает insert
    :param query: insert query
    :return: null
    """
    cnx = mysql.connector.connect(user='root', database='analytic_data_store', password="root")
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


def get_list_levels(request):
    # получение даных с бд
    data = __get_levels_from_db__("startgame")
    levels = dict()
    for key, value in data.items():
        json_data = json.loads(str(value["json_data"]).replace('"{', '{').replace('}"', '}'))
        levels[key] = (json_data["m_levelID"])

    return render(request, 'analytic_data/levels.html', {'levels': levels})


def __get_levels_from_db__(key_event):
    game_query = "SELECT id, key_event, json_data, user_secret_key, level_session_id " \
                 "FROM analytic_data_store.tesert_data WHERE key_event = '"+key_event+"';"
    cnx = mysql.connector.connect(user='root', database='analytic_data_store', password="root")
    cursor = cnx.cursor()

    data = dict()
    try:
        cursor.execute(game_query)
        for id, key_event, json_data, user_secret_key, level_session_id in cursor:
            data[id] = {"json_data": json_data, "user_secret_key": user_secret_key, "level_session_id": level_session_id}
    except Exception as mysql_error:
        print(mysql_error)
    finally:
        cursor.close()
        cnx.close()
        return data


def __get_level_from_db__(key_event):
    game_query = "SELECT id, key_event, json_data, user_secret_key, level_session_id " \
                 "FROM analytic_data_store.tesert_data WHERE  = '" + key_event + "';"
    cnx = mysql.connector.connect(user='root', database='analytic_data_store', password="root")
    cursor = cnx.cursor()

    data = dict()
    try:
        cursor.execute(game_query)
        for id, key_event, json_data, user_secret_key, level_session_id in cursor:
            data[id] = {"json_data": json_data, "user_secret_key": user_secret_key,
                        "level_session_id": level_session_id}
    except Exception as mysql_error:
        print(mysql_error)
    finally:
        cursor.close()
        cnx.close()
        return data