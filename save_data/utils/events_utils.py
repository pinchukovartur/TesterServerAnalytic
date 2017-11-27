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
            self.secondTarget = json_data["m_secondTarget"]
            self.seconds = json_data["m_seconds"]
            self.turns = json_data["m_turns"]

            self.game_components = ""
            if "m_Stat" in json_data.keys():
                self.game_components = GameComponents(json_data["m_Stat"])

            self.firstBonus = ""
            self.secondBonus = ""
            self.thirdBonus = ""
            self.userName = ""
            self.gameCurrency = ""
            if "m_gameCurrencyCount" in json_data.keys():
                self.gameCurrency = json_data["m_gameCurrencyCount"]
            if "m_firstBonus" in json_data.keys():
                self.firstBonus = json_data["m_firstBonus"]
            if "m_secondBonus" in json_data.keys():
                self.secondBonus = json_data["m_secondBonus"]
            if "m_thirdBonus" in json_data.keys():
                self.thirdBonus = json_data["m_thirdBonus"]
            if "m_userName" in json_data.keys():
                self.userName = json_data["m_userName"]


class GameComponents:
    def __init__(self, game_component):
        self.Color6_Red = ""
        self.Color6_Yellow = ""
        self.Color6_Blue = ""
        self.Color6_Green = ""
        self.Color6_White = ""
        self.Color6_Black = ""
        if "Color6_Red" in game_component.keys():
            Color6_Red = game_component["Color6_Red"]
            if Color6_Red:
                self.Color6_Red = Color6_Red
        if "Color6_Yellow" in game_component.keys():
            Color6_Yellow = game_component["Color6_Yellow"]
            if Color6_Yellow:
                self.Color6_Yellow = Color6_Yellow
        if "Color6_Blue" in game_component.keys():
            Color6_Blue = game_component["Color6_Blue"]
            if Color6_Blue:
                self.Color6_Blue = Color6_Blue
        if "Color6_Green" in game_component.keys():
            Color6_Green = game_component["Color6_Green"]
            if Color6_Green:
                self.Color6_Green = Color6_Green
        if "Color6_White" in game_component.keys():
            Color6_White = game_component["Color6_White"]
            if Color6_White:
                self.Color6_White = Color6_White
        if "Color6_Black" in game_component.keys():
            Color6_Black = game_component["Color6_Black"]
            if Color6_Black:
                self.Color6_Black = Color6_Black



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



