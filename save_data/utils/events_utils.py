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
        self.Color6_Red = 0
        self.Color6_Yellow = 0
        self.Color6_Blue = 0
        self.Color6_Green = 0
        self.Color6_White = 0
        self.Color6_Black = 0

        self.Super_FireSpark = 0
        self.Super_FireRing = 0
        self.Super_BigLightning_h = 0
        self.Super_BigLightning_v = 0
        self.Super_SmallLightning_v = 0
        self.Super_SmallLightning_h = 0
        self.Super_SphereOfFire = 0

        self.Stone = 0
        self.Weight = 0
        self.Lamp = 0
        self.Balloon = 0
        self.StarBonus = 0

        self.Box_Level1 = 0
        self.Box_Level2 = 0
        self.Box_Level3 = 0

        self.Carpet_Level1 = 0
        self.Carpet_Level2 = 0
        self.Carpet_Level3 = 0

        self.Chain_Level1 = 0
        self.Chain_Level2 = 0
        self.Chain_Level3 = 0

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

        if "Super_FireSpark" in game_component.keys():
            Super_FireSpark = game_component["Super_FireSpark"]
            if Super_FireSpark:
                self.Super_FireSpark = Super_FireSpark
        if "Super_FireRing" in game_component.keys():
            Super_FireRing = game_component["Super_FireRing"]
            if Super_FireRing:
                self.Super_FireRing = Super_FireRing
        if "Super_BigLightning_h" in game_component.keys():
            Super_BigLightning_h = game_component["Super_BigLightning_h"]
            if Super_BigLightning_h:
                self.Super_BigLightning_h = Super_BigLightning_h
        if "Super_BigLightning_v" in game_component.keys():
            Super_BigLightning_v = game_component["Super_BigLightning_v"]
            if Super_BigLightning_v:
                self.Super_BigLightning_v = Super_BigLightning_v
        if "Super_SmallLightning_v" in game_component.keys():
            Super_SmallLightning_v = game_component["Super_SmallLightning_v"]
            if Super_SmallLightning_v:
                self.Super_SmallLightning_v = Super_SmallLightning_v
        if "Super_SmallLightning_h" in game_component.keys():
            Super_SmallLightning_h = game_component["Super_SmallLightning_h"]
            if Super_SmallLightning_h:
                self.Super_SmallLightning_h = Super_SmallLightning_h
        if "Super_SphereOfFire" in game_component.keys():
            Super_SphereOfFire = game_component["Super_SphereOfFire"]
            if Super_SphereOfFire:
                self.Super_SphereOfFire = Super_SphereOfFire

        if "Box_Level1" in game_component.keys():
            Box_Level1 = game_component["Box_Level1"]
            if Box_Level1:
                self.Box_Level1 = Box_Level1
        if "Box_Level2" in game_component.keys():
            Box_Level2 = game_component["Box_Level2"]
            if Box_Level2:
                self.Box_Level2 = Box_Level2
        if "Box_Level3" in game_component.keys():
            Box_Level3 = game_component["Box_Level3"]
            if Box_Level3:
                self.Box_Level3 = Box_Level3

        if "Carpet_Level1" in game_component.keys():
            Carpet_Level1 = game_component["Carpet_Level1"]
            if Carpet_Level1:
                self.Carpet_Level1 = Carpet_Level1
        if "Carpet_Level2" in game_component.keys():
            Carpet_Level2 = game_component["Carpet_Level2"]
            if Carpet_Level2:
                self.Carpet_Level2 = Carpet_Level2
        if "Carpet_Level3" in game_component.keys():
            Carpet_Level3 = game_component["Carpet_Level3"]
            if Carpet_Level3:
                self.Carpet_Level3 = Carpet_Level3

        if "Chain_Level1" in game_component.keys():
            Chain_Level1 = game_component["Chain_Level1"]
            if Chain_Level1:
                self.Chain_Level1 = Chain_Level1
        if "Chain_Level2" in game_component.keys():
            Chain_Level2 = game_component["Chain_Level2"]
            if Chain_Level2:
                self.Chain_Level2 = Chain_Level2
        if "Chain_Level3" in game_component.keys():
            Chain_Level3 = game_component["Chain_Level3"]
            if Chain_Level3:
                self.Chain_Level3 = Chain_Level3

        if "Stone" in game_component.keys():
            Stone = game_component["Stone"]
            if Stone:
                self.Stone = Stone
        if "Weight" in game_component.keys():
            Weight = game_component["Weight"]
            if Weight:
                self.Weight = Weight
        if "Lamp" in game_component.keys():
            Lamp = game_component["Lamp"]
            if Lamp:
                self.Lamp = Lamp
        if "Balloon" in game_component.keys():
            Balloon = game_component["Balloon"]
            if Balloon:
                self.Balloon = Balloon
        if "StarBonus" in game_component.keys():
            StarBonus = game_component["StarBonus"]
            if StarBonus:
                self.Color6_Black = StarBonus


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
