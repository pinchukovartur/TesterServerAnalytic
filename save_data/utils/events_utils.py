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
            self.seconds = '-1'#json_data["m_seconds"] //nikolayku; time was removed from games
            self.turns = json_data["m_turns"]

            self.game_components = ""
            if "m_Stat" in json_data.keys():
                self.game_components = GameComponents(json_data["m_Stat"])

            self.firstBonus = ""
            self.secondBonus = ""
            self.thirdBonus = ""
            self.userName = ""
            self.gameCurrency = ""
            self.countUseBombBonys = ""
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
            if "m_countUseBombBonys" in json_data.keys():
                self.countUseBombBonys = json_data["m_countUseBombBonys"]


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
        self.Super_SmallLightning = 0
        self.Super_SphereOfFire = 0

        self.Stone = 0
        self.Weight = 0
        self.Lamp = 0
        self.Balloon = 0
        self.StarBonus = 0
        self.CrystalBall = 0
        self.Sand = 0

        self.Box_Level1 = 0
        self.Box_Level2 = 0
        self.Box_Level3 = 0

        self.Carpet_Level1 = 0
        self.Carpet_Level2 = 0
        self.Carpet_Level3 = 0

        self.Chain_Level1 = 0
        self.Chain_Level2 = 0
        self.Chain_Level3 = 0

        self.Diamond_Level1 = 0
        self.Diamond_Level2 = 0
        self.Diamond_Level3 = 0

        self.Granite_Level1 = 0
        self.Granite_Level2 = 0

        self.Ice_Level1 = 0
        self.Ice_Level2 = 0

        self.MultiStoneLevel1 = 0
        self.MultiStoneLevel2 = 0
        self.MultiStoneLevel3 = 0

        self.Bear = 0
        self.ChipMoves = 0
        self.GunShot = 0

        self.FenceDestroy = 0
        self.PearlBank = 0
        self.SandBank = 0
        self.Gift = 0

        self.FlowerGreen = 0
        self.FlowerRed = 0
        self.FlowerWhite = 0
        self.FlowerBlack = 0
        self.FlowerBlue = 0
        self.FlowerYellow = 0

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
                self.Super_SmallLightning += Super_SmallLightning_v
        if "Super_SmallLightning_h" in game_component.keys():
            Super_SmallLightning_h = game_component["Super_SmallLightning_h"]
            if Super_SmallLightning_h:
                self.Super_SmallLightning += Super_SmallLightning_h
        if "Super_SphereOfFire" in game_component.keys():
            Super_SphereOfFire = game_component["Super_SphereOfFire"]
            if Super_SphereOfFire:
                self.Super_SphereOfFire = Super_SphereOfFire

        if "Diamond_Level1" in game_component.keys():
            Diamond_Level1 = game_component["Diamond_Level1"]
            if Diamond_Level1:
                self.Diamond_Level1 = Diamond_Level1
        if "Diamond_Level2" in game_component.keys():
            Diamond_Level2 = game_component["Diamond_Level2"]
            if Diamond_Level2:
                self.Diamond_Level2 = Diamond_Level2
        if "Diamond_Level3" in game_component.keys():
            Diamond_Level3 = game_component["Diamond_Level3"]
            if Diamond_Level3:
                self.Diamond_Level3 = Diamond_Level3

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
                self.StarBonus = StarBonus
        if "CrystalBall" in game_component.keys():
            CrystalBall = game_component["CrystalBall"]
            if CrystalBall:
                self.CrystalBall = CrystalBall
        if "Sand" in game_component.keys():
            Sand = game_component["Sand"]
            if Sand:
                self.Sand = Sand

        if "Granite_Level1" in game_component.keys():
            Granite_Level1 = game_component["Granite_Level1"]
            if Granite_Level1:
                self.Granite_Level1 = Granite_Level1
        if "Granite_Level2" in game_component.keys():
            Granite_Level2 = game_component["Granite_Level2"]
            if Granite_Level2:
                self.Granite_Level2 = Granite_Level2

        if "Ice_Level1" in game_component.keys():
            Ice_Level1 = game_component["Ice_Level1"]
            if Ice_Level1:
                self.Ice_Level1 = Ice_Level1
        if "Ice_Level2" in game_component.keys():
            Ice_Level2 = game_component["Ice_Level2"]
            if Ice_Level2:
                self.Ice_Level2 = Ice_Level2

        if "MultilevelStone_Level1" in game_component.keys():
            MultiStoneLevel1 = game_component["MultilevelStone_Level1"]
            if MultiStoneLevel1:
                self.MultiStoneLevel1 = MultiStoneLevel1
        if "MultilevelStone_Level2" in game_component.keys():
            MultiStoneLevel2 = game_component["MultilevelStone_Level2"]
            if MultiStoneLevel2:
                self.MultiStoneLevel2 = MultiStoneLevel2
        if "MultilevelStone_Level3" in game_component.keys():
            MultiStoneLevel3 = game_component["MultilevelStone_Level3"]
            if MultiStoneLevel3:
                self.MultiStoneLevel3 = MultiStoneLevel3

        if "Bear" in game_component.keys():
            Bear = game_component["Bear"]
            if Bear:
                self.Bear = Bear
        if "ChipMoves" in game_component.keys():
            ChipMoves = game_component["ChipMoves"]
            if ChipMoves:
                self.ChipMoves = ChipMoves
        if "GunShot" in game_component.keys():
            GunShot = game_component["GunShot"]
            if GunShot:
                self.GunShot = GunShot

        if "ChipMoves_Red" in game_component.keys():
            ChipMoves = game_component["ChipMoves_Red"]
            if ChipMoves:
                self.ChipMoves += ChipMoves

        if "ChipMoves_Blue" in game_component.keys():
            ChipMoves = game_component["ChipMoves_Blue"]
            if ChipMoves:
                self.ChipMoves += ChipMoves

        if "ChipMoves_Black" in game_component.keys():
            ChipMoves = game_component["ChipMoves_Black"]
            if ChipMoves:
                self.ChipMoves += ChipMoves

        if "ChipMoves_Yellow" in game_component.keys():
            ChipMoves = game_component["ChipMoves_Yellow"]
            if ChipMoves:
                self.ChipMoves += ChipMoves

        if "ChipMoves_White" in game_component.keys():
            ChipMoves = game_component["ChipMoves_White"]
            if ChipMoves:
                self.ChipMoves += ChipMoves

        if "ChipMoves_Green" in game_component.keys():
            ChipMoves = game_component["ChipMoves_Green"]
            if ChipMoves:
                self.ChipMoves += ChipMoves

        if "DestroyFence" in game_component.keys():
            FenceDestroy = game_component["DestroyFence"]
            if FenceDestroy:
                self.FenceDestroy = FenceDestroy

        if "FlyPearl" in game_component.keys():
            PearlBank = game_component["FlyPearl"]
            if PearlBank:
                self.PearlBank = PearlBank

        if "SandBank" in game_component.keys():
            SandBank = game_component["SandBank"]
            if SandBank:
                self.SandBank = SandBank

        if "GiftExplosion" in game_component.keys():
            Gift = game_component["GiftExplosion"]
            if Gift:
                self.Gift = Gift

        if "Flower_Green" in game_component.keys():
            FlowerGreen = game_component["Flower_Green"]
            if FlowerGreen:
                self.FlowerGreen = FlowerGreen

        if "Flower_Black" in game_component.keys():
            FlowerBlack = game_component["Flower_Black"]
            if FlowerBlack:
                self.FlowerBlack = FlowerBlack

        if "Flower_Red" in game_component.keys():
            FlowerRed = game_component["Flower_Red"]
            if FlowerRed:
                self.FlowerRed = FlowerRed

        if "Flower_White" in game_component.keys():
            FlowerWhite = game_component["Flower_White"]
            if FlowerWhite:
                self.FlowerWhite = FlowerWhite

        if "Flower_Yellow" in game_component.keys():
            FlowerYellow = game_component["Flower_Yellow"]
            if FlowerYellow:
                self.FlowerYellow = FlowerYellow

        if "Flower_Blue" in game_component.keys():
            FlowerBlue = game_component["Flower_Blue"]
            if FlowerBlue:
                self.FlowerBlue = FlowerBlue

        #for vail in game_component.keys():
        #    print(vail)


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


def get_levels_with_min_date():
    levels = get_levels()

    for key in levels.keys():

        data = 0

        for event in levels[key]:
            if event.level_info.levelID in data:
                if data > event.event_datetime:
                    data = {event.event_datetime, 0}
            else:
                data = (event.event_datetime, 0)

        tmp = list()
        tmp.append(levels[key])
        tmp.append(data)

        levels[key] = tmp

    return levels


def get_event_by_session_key(events, level_key):
    for event in events:
        if event.level_session_id == level_key:
            return event
    return None


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


def get_event_by_lvl_name(lvl_name):
    events = get_events()
    lvl_events = list()
    for event in events:
        if event.level_info.levelID == lvl_name:
            lvl_events.append(event)

    return lvl_events


def get_levels():
    levels = dict()
    events = get_events()
    for event in events:
        if event.level_info.levelID in levels:
            levels[event.level_info.levelID].append(event)
        else:
            levels[event.level_info.levelID] = list()
            levels[event.level_info.levelID].append(event)

    return levels


def get_count_exit_game(level_name):
    levels = get_levels()

    if level_name not in levels.keys():
        return None

    exit_count = 0

    without_finish = 0

    start_game_events = list()
    target_complete_events = list()
    level_complete_events = list()
    fail_game_events = list()

    for lvl_event in levels[level_name]:
            if lvl_event.key_event == "startgame":
                start_game_events.append(lvl_event)
            elif lvl_event.key_event == "failgame":
                fail_game_events.append(lvl_event)
            elif lvl_event.key_event == "completegame":
                target_complete_events.append(lvl_event)
            elif lvl_event.key_event == "finishlevel":
                level_complete_events.append(lvl_event)

    for start_event in start_game_events:

        fail_event = get_event_by_session_key(fail_game_events, start_event.level_session_id)
        if fail_event is None:
            target_complete_event = get_event_by_session_key(target_complete_events, start_event.level_session_id)
            if target_complete_event is None:
                exit_count += 1

        complete_event = get_event_by_session_key(level_complete_events, start_event.level_session_id)
        if complete_event is None and fail_event is None:
            without_finish += 1

    return level_name, exit_count, without_finish - exit_count
