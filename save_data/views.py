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
    data = __get_events_from_db__("startgame")
    levels = set()
    for key, value in data.items():
        json_data = json.loads(str(value["json_data"]).replace('"{', '{').replace('}"', '}'))
        levels.add(json_data["m_levelID"])

    return render(request, 'analytic_data/levels.html', {'levels': levels})


def get_level(request):
    # получение даных с бд
    level_name = request.GET['level_name']

    data = __get_events_from_db__("startgame")

    # получаем pk всех ивентов, которые содержат level_name
    level_events = dict()
    for key, value in data.items():
        value["event_data"] = json.loads(str(value["json_data"]).replace('"{', '{').replace('}"', '}'))
        value["json_data"] = None
        if value["event_data"]["m_levelID"] == level_name:

            # проверяем, были ли они окончены
            final_event = __get_final_event__(value["level_session_id"])
            if final_event:

                # добавляем финальный event
                for key_final_event, value_final_event in final_event.items():
                    value_final_event["event_data"] = json.loads(str(value_final_event["json_data"]).replace('"{', '{').replace('}"', '}'))
                    value_final_event["json_data"] = None
                    event_dict = dict()
                    event_dict["startevent"] = value
                    event_dict["endevent"] = value_final_event
                    level_events[key] = event_dict


        data_level = dict()
        count = 0
        for key, value in level_events.items():
            return_dict = dict()
            return_dict["starttime"] = value["startevent"]["event_datetime"]
            return_dict["endtime"] = value["endevent"]["event_datetime"]

            # try
            count += 1
            return_dict["try"] = count

            # complete/fail
            return_dict["result"] = value["endevent"]["key_event"]

            # targets
            return_dict["wasturns"] = value["endevent"]["event_data"]["m_turns"]
            return_dict["wasseconds"] = value["endevent"]["event_data"]["m_seconds"]

            return_dict["turns"] = value["startevent"]["event_data"]["m_turns"]
            return_dict["seconds"] = value["startevent"]["event_data"]["m_seconds"]

            if value["endevent"]["event_data"]["m_firstTarget"]["m_type"] != "":
                return_dict["target1"] = value["endevent"]["event_data"]["m_firstTarget"]
            if value["endevent"]["event_data"]["m_secondTarget"]["m_type"] != "":
                return_dict["target2"] = value["endevent"]["event_data"]["m_secondTarget"]

            data_level[key] = return_dict
    #print(level_events)
    return render(request, 'analytic_data/level.html', {'events': data_level})
"""
            # try
            count += 1
            return_dict["try"] = count

            # complete/fail
            return_dict["result"] = value["endevent"]["key_event"]

            # targets
            return_dict["wasturns"] = value["endevent"]["event_data"]["m_turns"]
            return_dict["wasseconds"] = value["endevent"]["event_data"]["m_seconds"]

            return_dict["turns"] = value["startevent"]["event_data"]["m_turns"]
            return_dict["seconds"] = value["startevent"]["event_data"]["m_seconds"]
            if value["endevent"]["event_data"]["m_firstTarget"]["m_type"] != "":
                return_dict["target1"] = value["endevent"]["event_data"]["m_firstTarget"]
            if value["endevent"]["event_data"]["m_secondTarget"]["m_type"] != "":
                return_dict["target2"] = value["endevent"]["event_data"]["m_secondTarget"]
"""






def __get_events_from_db__(key_event):
    game_query = "SELECT id, key_event, json_data, user_secret_key, level_session_id, event_datetime " \
                 "FROM analytic_data_store.tester_data WHERE key_event = '" + key_event + "';"
    cnx = mysql.connector.connect(user='root', database='analytic_data_store', password="root")
    cursor = cnx.cursor()

    data = dict()
    try:
        cursor.execute(game_query)
        for id, key_event, json_data, user_secret_key, level_session_id, event_datetime in cursor:
            data[id] = {"json_data": json_data, "user_secret_key": user_secret_key, "key_event": key_event,
                        "level_session_id": level_session_id, "event_datetime": event_datetime}
    except Exception as mysql_error:
        print(mysql_error)
    finally:
        cursor.close()
        cnx.close()
        return data


def __get_final_event__(session_key):
    game_query = "SELECT id, key_event, json_data, user_secret_key, level_session_id, event_datetime" \
                 " FROM analytic_data_store.tester_data" \
                 " WHERE key_event != 'startgame' and level_session_id = '" + session_key + "';"
    cnx = mysql.connector.connect(user='root', database='analytic_data_store', password="root")
    cursor = cnx.cursor()

    final_event = dict()
    try:
        cursor.execute(game_query)
        for id, key_event, json_data, user_secret_key, level_session_id, event_datetime in cursor:
            final_event[id] = {"json_data": json_data, "user_secret_key": user_secret_key, "key_event": key_event,
                               "level_session_id": level_session_id, "event_datetime": event_datetime}
    except Exception as mysql_error:
        print(mysql_error)
    finally:
        cursor.close()
        cnx.close()

    if len(final_event) == 1:
        return final_event
    elif len(final_event) > 1:
        raise NameError("> 1 level finish, check validate data base")


def __get_analytic_data(level_events):
    pass