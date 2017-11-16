from django.http import HttpResponse
import mysql.connector

# the method return user script
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import json
import collections


@csrf_exempt
def save_data(request):
    try:
        key = request.POST['key']
        data = request.POST['data']
        user_secret_key = request.POST['user_secret_key']
        level_session_id = request.POST['level_session_id']

        query = "INSERT INTO analytic_data_store.tester_data (key_event, json_data, user_secret_key, level_session_id)" \
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
    if len(levels) == 0:
        return HttpResponse("Levels Not Found")
    return render(request, 'analytic_data/levels.html', {'levels': levels})


def get_level(request):
    # получение даных с бд
    global events_data, try_count, common_data, complete_count, fail_count, spent_turn_count, spent_second_count, target1_count, target2_count, give_turn_count, give_second_count, event_data, target2sent_count, target1sent_count
    level_name = request.GET['level_name']

    data = __get_events_from_db__("startgame")
    # sort
    #data = collections.OrderedDict(sorted(data.items()))
    # получаем pk всех ивентов, которые содержат level_name
    level_events = dict()
    event_key = 1
    for key, value in data.items():
        value["event_data"] = json.loads(str(value["json_data"]).replace('"{', '{').replace('}"', '}'))
        value["json_data"] = None
        if value["event_data"]["m_levelID"] == level_name:

            # проверяем, были ли они окончены
            final_event = __get_final_event__(value["level_session_id"])
            if final_event:

                # добавляем финальный event
                for key_final_event, value_final_event in final_event.items():
                    value_final_event["event_data"] = json.loads(
                        str(value_final_event["json_data"]).replace('"{', '{').replace('}"', '}'))
                    value_final_event["json_data"] = None
                    event_dict = dict()
                    event_dict["startevent"] = value
                    event_dict["endevent"] = value_final_event
                    level_events[key] = event_dict
                    event_key += 1

        events_data = dict()
        count = 0

        common_data = dict()

        try_count = list()
        complete_count = list()
        fail_count = list()
        spent_turn_count = list()
        spent_second_count = list()
        give_turn_count = list()
        give_second_count = list()
        target1sent_count = list()
        target1_count = list()
        target2_count = list()
        target2sent_count = list()
        level_events = collections.OrderedDict(sorted(level_events.items()))
        for key, value in level_events.items():
            event_data = dict()
            event_data["starttime"] = value["startevent"]["event_datetime"]
            event_data["endtime"] = value["endevent"]["event_datetime"]

            # try
            count += 1
            event_data["try"] = count
            try_count.append(count)

            # complete/fail
            if value["endevent"]["key_event"] == "completegame":
                event_data["completegame"] = 1
                complete_count.append(1)
            elif value["endevent"]["key_event"] == "failgame":
                event_data["failgame"] = 1
                fail_count.append(1)

            # targets
            # spent
            spent_second = int(value["endevent"]["event_data"]["m_seconds"])
            if spent_second > 0:
                event_data["wasseconds"] = spent_second
                spent_second_count.append(spent_second)
            spent_turn = int(value["endevent"]["event_data"]["m_turns"])
            if spent_turn > 0:
                event_data["wasturns"] = spent_turn
                spent_turn_count.append(spent_turn)
            # given
            give_second = int(value["startevent"]["event_data"]["m_seconds"])
            if give_second > 0:
                event_data["seconds"] = give_second
                give_second_count.append(give_second)
            give_turn = int(value["startevent"]["event_data"]["m_turns"])
            if give_turn > 0:
                event_data["turns"] = give_turn
                give_turn_count.append(give_turn)

            target1 = int(value["endevent"]["event_data"]["m_firstTarget"]["m_required"])
            if target1 > 0:
                # m_required - надо было собрать,   m_remainder - было собрано
                target1_count.append(target1)
                event_data["target1"] = str(target1)
                event_data["target1type"] = value["endevent"]["event_data"]["m_firstTarget"]["m_type"]
            target2 = int(value["endevent"]["event_data"]["m_secondTarget"]["m_required"])
            if target2 > 0:
                # m_required - надо было собрать,   m_remainder - было собрано
                target2_count.append(target2)
                event_data["target2"] = str(target2)
                event_data["target2type"] = value["endevent"]["event_data"]["m_secondTarget"]["m_type"]

            target1sent = int(value["endevent"]["event_data"]["m_firstTarget"]["m_remainder"])
            if target1sent > 0:
                target1sent_count.append(target1sent)
                event_data["target1sent"] = str(target1sent)
            target2sent = int(value["endevent"]["event_data"]["m_secondTarget"]["m_remainder"])
            print(value["endevent"]["event_data"]["m_secondTarget"])
            if target2sent > 0:
                target2sent_count.append(target2sent)
                event_data["target2sent"] = str(target2sent)

            events_data[len(events_data) + 1] = event_data

    common_data["complete"] = sum(complete_count)
    common_data["fail"] = sum(fail_count)
    if len(spent_turn_count) > 0:
        common_data["spent_turn"] = str(float(sum(spent_turn_count) / len(spent_turn_count))) + " +- " \
                                + str((max(spent_turn_count) - min(spent_turn_count)) / 2)
    if len(spent_second_count) > 0:
        common_data["spent_second"] = str(float(sum(spent_second_count) / len(spent_second_count))) + " +- " \
                                + str((max(spent_second_count) - min(spent_second_count)) / 2)
    if len(target1_count) > 0:
        common_data["target1"] = str(float(sum(target1_count) / len(target1_count))) + " +- " \
                                + str((max(target1_count) - min(target1_count)) / 2)
    if len(target2_count) > 0:
        common_data["target2"] = str(float(sum(target2_count) / len(target2_count))) + " +- " \
                                + str((max(target2_count) - min(target2_count)) / 2)
    if len(target1sent_count) > 0:
        common_data["target1sent"] = str(float(sum(target1sent_count) / len(target1sent_count))) + " +- " \
                                + str((max(target1sent_count) - min(target1sent_count)) / 2)
    if len(target2sent_count) > 0:
        common_data["target2sent"] = str(float(sum(target2sent_count) / len(target2sent_count))) + " +- " \
                                + str((max(target2sent_count) - min(target2sent_count)) / 2)
    if len(spent_turn_count) > 0:
        common_data["spent_turn"] = str(float(sum(spent_turn_count) / len(spent_turn_count))) + " +- " \
                                + str((max(spent_turn_count) - min(spent_turn_count)) / 2)
    if len(give_turn_count) > 0:
        common_data["give_turn"] = str(float(sum(give_turn_count) / len(give_turn_count))) + " +- " \
                                + str((max(give_turn_count) - min(give_turn_count)) / 2)
    if len(give_second_count) > 0:
        common_data["give_second"] = str(float(sum(give_second_count) / len(give_second_count))) + " +- " \
                                + str((max(give_second_count) - min(give_second_count)) / 2)

    return render(request, 'analytic_data/level.html', {'events': events_data, "common_data": common_data,
                                                        "target1": event_data["target1type"],
                                                        "target2": event_data["target2type"]})


def __get_events_from_db__(key_event):
    game_query = "SELECT id, key_event, json_data, user_secret_key, level_session_id, event_datetime " \
                 "FROM analytic_data_store.tester_data WHERE key_event = '" + key_event + "' order by event_datetime;"
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
                 " WHERE key_event != 'startgame' and level_session_id = '" + session_key + "' order by event_datetime;"
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
