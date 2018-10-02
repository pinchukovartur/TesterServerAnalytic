from django.http import HttpResponse
from django.shortcuts import redirect
import mysql.connector
import datetime

# the method return user script
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

from save_data.utils.db_utils import insert, delete
from save_data.utils.events_utils import get_events, sort_by_key_event, sort_by_event_datetime, \
    delete_copy_event_with_big_date, sort_by_date_time, get_count_exit_game

from save_data.utils.analytic_utils import get_analytic_data


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
    return render(request, 'analytic_data/index.html')


def __get_sorted_levels():
    events = get_events()
    start_game_events = sort_by_key_event(events, "startgame")
    dict_level_info = delete_copy_event_with_big_date(start_game_events)
    return sorted(dict_level_info.items(), key=lambda p: p[1])


def get_list_levels(request):
    set_level_info = __get_sorted_levels()
    print(len(set_level_info))
    #set_level_info = sorted(set_level_info, key=lambda x: x[0])
    date_type = "rev"
    name_type = "simple"
    if "sort" in request.GET.keys():
        sort = request.GET["sort"]

        if sort == "date":
            if "type" in request.GET.keys():
                date_type = request.GET["type"]
                if date_type == "rev":
                    set_level_info = reversed(set_level_info)
                    date_type = "simple"
                else:
                    date_type = "rev"
        if sort == "name":
            if "type" in request.GET.keys():
                name_type = request.GET["type"]
                if name_type == "rev":
                    set_level_info = reversed(sorted(set_level_info, key=lambda x: x[0]))
                    name_type = "simple"
                else:
                    name_type = "rev"
                    set_level_info = sorted(set_level_info, key=lambda x: x[0])

    return render(request, 'analytic_data/levels.html', {'levels': set_level_info, "date_type": date_type,  "name_type": name_type})


def delete_events(request):
    event_id = request.GET.get('event_id', "")
    level_name = request.GET.get('level_name', "")
    if event_id == "" or level_name == "":
        return HttpResponse("event_id or level_name cannot be null")
    delete(event_id)
    return redirect("/levels/level?level_name=" + level_name)


def sort_levels(request):
    print("aaaa")
    set_level_info = __get_sorted_levels()

    until_date = request.GET.get('until', "12/12/3012 0:00 PM")
    from_date = request.GET.get('from', "12/12/2012 0:00 PM")


    return render(request, 'analytic_data/levels.html',
                  {'levels': sort_by_date_time(from_date, until_date, set_level_info)})


def get_level(request):
    level_name = request.GET.get('level_name', "")
    if level_name == "":
        return HttpResponse("Level Not Found")

    analytic_data, total_data, list_secret_key_date = get_analytic_data(level_name)
    if len(analytic_data) == 0:
        return HttpResponse("Level Event Not Found")

    level_info = get_count_exit_game(level_name)


    return render(request, 'analytic_data/level.html', {'events': analytic_data, "common_data": total_data,
                                                        "list_secret_key_date": list_secret_key_date,
                                                        "level_info": level_info})
