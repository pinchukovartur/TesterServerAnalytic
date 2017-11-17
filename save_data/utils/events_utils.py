import json
import operator
import datetime
from save_data.utils.db_utils import get_events_from_db


class LevelInfo:
    def __init__(self, level_info_json):
        json_data = json.loads(str(level_info_json).replace('"{', '{').replace('}"', '}'))
        if json_data:
            self.levelID = json_data["m_levelID"]
            self.firstTarget = json_data["m_firstTarget"]
            self.seconds = json_data["m_secondTarget"]


class Event:
    def __init__(self, id, key_event, json_data, user_secret_key, level_session_id, event_datetime):
        self.id = id
        self.key_event = key_event
        self.level_info = LevelInfo(json_data)
        self.user_secret_key = user_secret_key
        self.level_session_id = level_session_id
        self.event_datetime = event_datetime


def get_events():
    events = get_events_from_db()
    list_events = list()
    for key, value in events.items():
        list_events.append(Event(key, value["key_event"], value["json_data"], value["user_secret_key"],
                                 value["level_session_id"], value["event_datetime"]))
    return list_events


def sort_by_key_event(events, key_event):
    sort_list = list()
    for event in events:
        if event.key_event == key_event:
            sort_list.append(event)
    return sort_list


def sort_by_event_datetime(events):
    return sorted(events, key=operator.attrgetter("event_datetime"))


def delete_copy_event_with_big_date(events):
    level_date = dict()
    for event in events:
        if event.level_info.levelID in level_date:
            if level_date[event.level_info.levelID] > event.event_datetime:
                level_date[event.level_info.levelID] = event.event_datetime
        else:
            level_date[event.level_info.levelID] = event.event_datetime
    return level_date


def sort_by_date_time(from_date, until_date, set_level_info):
    if from_date:
        from_date = datetime.datetime.strptime(str(from_date), "%m/%d/%Y %H:%M %p")
    if until_date:
        until_date = datetime.datetime.strptime(str(until_date), "%m/%d/%Y %H:%M %p")

    if from_date:
        sort_levels = list()
        for value in set_level_info:
            if value[1] > from_date:
                sort_levels.append(value)
        set_level_info = sort_levels
    if until_date:
        sort_levels = list()
        for value in set_level_info:
            if value[1] < until_date:
                sort_levels.append(value)
        set_level_info = sort_levels
    return set_level_info


def get_analytic_data(level_name):
    events = get_events()

    level_events = list()
    for event in events:
        if event.level_info.levelID == level_name:
            level_events.append(event)

    finished_levels = list()
    for lvl_event_i in level_events:
        for lvl_event_j in level_events:
            if lvl_event_i.key_event == "startgame" and lvl_event_j.key_event != "startgame" and lvl_event_i.level_session_id == lvl_event_j.level_session_id:
                finished_levels.append((lvl_event_i, lvl_event_j))





    return finished_levels

