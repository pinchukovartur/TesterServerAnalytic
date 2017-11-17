from django.http import HttpResponse
import mysql.connector

# the method return user script
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import json
import collections
import datetime
import operator

from save_data.utils.db_utils import insert
from save_data.utils.events_utils import get_events, sort_by_key_event, sort_by_event_datetime, \
    delete_copy_event_with_big_date, sort_by_date_time, get_analytic_data


@csrf_exempt
def save_data(request):
    try:
        key = request.POST['key']
        data = request.POST['data']
        user_secret_key = request.POST['user_secret_key']
        level_session_id = request.POST['level_session_id']

        query = "INSERT INTO analytic_data_store.tester_data (key_event, json_data, user_secret_key, level_session_id)" \
                " VALUES('" + key + "', '" + data + "', '" + user_secret_key + "', '" + level_session_id + "'); "
        insert(query)

    except Exception as error:
        print(error)
        return HttpResponse(str(error))

    return HttpResponse("200")


def index(request):
    print(len())
    return render(request, 'analytic_data/index.html')


def __get_sorted_levels():
    events = get_events()
    start_game_events = sort_by_key_event(events, "startgame")
    dict_level_info = delete_copy_event_with_big_date(start_game_events)
    return sorted(dict_level_info.items(), key=lambda p: p[1])


def get_list_levels(request):
    set_level_info = __get_sorted_levels()
    return render(request, 'analytic_data/levels.html', {'levels': set_level_info})


def sort_levels(request):
    set_level_info = __get_sorted_levels()

    until_date = request.GET.get('until', "12/12/3012 0:00 PM")
    from_date = request.GET.get('from', "12/12/2012 0:00 PM")

    return render(request, 'analytic_data/levels.html',
                  {'levels': sort_by_date_time(from_date, until_date, set_level_info)})


def get_level(request):
    level_name = request.GET.get('level_name', "")
    if level_name == "":
        return HttpResponse("Level Not Found")

    print(get_analytic_data(level_name)[0][0].level_info.firstTarget)
    list_events = get_analytic_data(level_name)
    return render(request, 'analytic_data/level.html', {'events': list_events})

    """
    # получение даных с бд
    global events_data, try_count, common_data, complete_count, fail_count, spent_turn_count, spent_second_count, \
        target1_count, target2_count, give_turn_count, give_second_count, event_data, target2sent_count, \
        target1sent_count



    events = get_events()
    data = sort_by_key_event(events, "startgame")


    level_events = dict()
    event_key = 1
    for key, value in data.items():
        value["event_data"] = json.loads(str(value["json_data"]).replace('"{', '{').replace('}"', '}'))
        value["json_data"] = None
        if value["event_data"]["m_levelID"] == level_name:

            # проверяем, были ли они окончены
            final_event = __get_failgame_event__(value["level_session_id"])
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
            event_data["target1type"] = ""
            if target1 > 0:
                # m_required - надо было собрать,   m_remainder - было собрано
                target1_count.append(target1)
                event_data["target1"] = str(target1)
                event_data["target1type"] = value["endevent"]["event_data"]["m_firstTarget"]["m_type"]
            target2 = int(value["endevent"]["event_data"]["m_secondTarget"]["m_required"])
            event_data["target2type"] = ""
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
            if target2sent > 0:
                target2sent_count.append(target2sent)
                event_data["target2sent"] = str(target2sent)

            events_data[len(events_data) + 1] = event_data
    if len(events_data) == 0:
        return HttpResponse("level not found: 232")
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

    return render(request, 'analytic_data/level.html', {'events': events_data, "common_data": common_data,
                                                        "target1": event_data["target1type"],
                                                        "target2": event_data["target2type"]})
                                     + str((max(give_second_count) - min(give_second_count)) / 2)
"""

def __get_failgame_event__(session_key):
    game_query = "SELECT id, key_event, json_data, user_secret_key, level_session_id, event_datetime" \
                 " FROM analytic_data_store.tester_data" \
                 " WHERE key_event != 'finishlevel' and key_event != 'startgame' and level_session_id = '" + session_key + "' order by event_datetime;"
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


def __get_level_finish_event__(session_key):
    game_query = "SELECT id, key_event, json_data, user_secret_key, level_session_id, event_datetime" \
                 " FROM analytic_data_store.tester_data" \
                 " WHERE key_event = 'finishlevel' and level_session_id = '" + session_key + "' order by event_datetime;"
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

    if len(final_event) == 2:
        return final_event
    elif len(final_event) > 2:
        raise NameError("> 1 level finish, check validate data base")
