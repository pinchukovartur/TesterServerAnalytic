from save_data.utils.events_utils import get_events, get_event_by_session_key
from numpy import var, median
import datetime


class AnalyticEvenData:
    def __init__(self, start_event, finish_event, lvl_end_event, level_name):

        self.level_name = level_name
        self.start_date = ""
        self.end_date = ""

        self.level_session_id = ""

        self.target1_name = ""
        self.target1_count = ""
        self.target2_name = ""
        self.target2_count = ""

        self.spent_turn = 0
        self.spent_second = 0
        self.give_turn = 0
        self.give_seconds = 0

        self.left_turn = ''

        self.fail_game = 0
        self.win_game = 0

        self.first_bonus = 0
        self.second_bonus = 0
        self.third_bonus = 0

        self.game_currency = ""

        self.target1_count_collected = ""
        self.target2_count_collected = ""

        # self.target1_count_overflow = ""
        # self.target2_count_overflow = ""

        self.countUseBombBonys = 0

        self.diff_time = ""
        self.user_name = ""

        self.red = 0
        self.yellow = 0
        self.blue = 0
        self.green = 0
        self.white = 0
        self.black = 0

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

        if finish_event.level_info.game_components:
            if str(finish_event.level_info.game_components.Color6_Red):
                self.red = int(finish_event.level_info.game_components.Color6_Red)
            if str(finish_event.level_info.game_components.Color6_Yellow):
                self.yellow = int(finish_event.level_info.game_components.Color6_Yellow)
            if str(finish_event.level_info.game_components.Color6_Blue):
                self.blue = int(finish_event.level_info.game_components.Color6_Blue)
            if str(finish_event.level_info.game_components.Color6_Green):
                self.green = int(finish_event.level_info.game_components.Color6_Green)
            if str(finish_event.level_info.game_components.Color6_White):
                self.white = int(finish_event.level_info.game_components.Color6_White)
            if str(finish_event.level_info.game_components.Color6_Black):
                self.black = int(finish_event.level_info.game_components.Color6_Black)

            if str(finish_event.level_info.game_components.Super_FireSpark):
                self.Super_FireSpark = int(finish_event.level_info.game_components.Super_FireSpark)
            if str(finish_event.level_info.game_components.Super_FireRing):
                self.Super_FireRing = int(finish_event.level_info.game_components.Super_FireRing)
            if str(finish_event.level_info.game_components.Super_BigLightning_h):
                self.Super_BigLightning_h = int(finish_event.level_info.game_components.Super_BigLightning_h)
            if str(finish_event.level_info.game_components.Super_BigLightning_v):
                self.Super_BigLightning_v = int(finish_event.level_info.game_components.Super_BigLightning_v)
            if str(finish_event.level_info.game_components.Super_SmallLightning):
                self.Super_SmallLightning = int(finish_event.level_info.game_components.Super_SmallLightning)
            if str(finish_event.level_info.game_components.Super_SphereOfFire):
                self.Super_SphereOfFire = int(finish_event.level_info.game_components.Super_SphereOfFire)

            if str(finish_event.level_info.game_components.Stone):
                self.Stone = int(finish_event.level_info.game_components.Stone)
            if str(finish_event.level_info.game_components.Weight):
                self.Weight = int(finish_event.level_info.game_components.Weight)
            if str(finish_event.level_info.game_components.Lamp):
                self.Lamp = int(finish_event.level_info.game_components.Lamp)
            if str(finish_event.level_info.game_components.Balloon):
                self.Balloon = int(finish_event.level_info.game_components.Balloon)
            if str(finish_event.level_info.game_components.StarBonus):
                self.StarBonus = int(finish_event.level_info.game_components.StarBonus)
            if str(finish_event.level_info.game_components.CrystalBall):
                self.CrystalBall = int(finish_event.level_info.game_components.CrystalBall)
            if str(finish_event.level_info.game_components.Sand):
                self.Sand = int(finish_event.level_info.game_components.Sand)

            if str(finish_event.level_info.game_components.Diamond_Level1):
                self.Diamond_Level1 = int(finish_event.level_info.game_components.Diamond_Level1)
            if str(finish_event.level_info.game_components.Diamond_Level2):
                self.Diamond_Level2 = int(finish_event.level_info.game_components.Diamond_Level2)
            if str(finish_event.level_info.game_components.Diamond_Level3):
                self.Diamond_Level3 = int(finish_event.level_info.game_components.Diamond_Level3)

            if str(finish_event.level_info.game_components.Box_Level1):
                self.Box_Level1 = int(finish_event.level_info.game_components.Box_Level1)
            if str(finish_event.level_info.game_components.Box_Level2):
                self.Box_Level2 = int(finish_event.level_info.game_components.Box_Level2)
            if str(finish_event.level_info.game_components.Box_Level3):
                self.Box_Level3 = int(finish_event.level_info.game_components.Box_Level3)

            if str(finish_event.level_info.game_components.Carpet_Level1):
                self.Carpet_Level1 = int(finish_event.level_info.game_components.Carpet_Level1)
            if str(finish_event.level_info.game_components.Carpet_Level2):
                self.Carpet_Level2 = int(finish_event.level_info.game_components.Carpet_Level2)
            if str(finish_event.level_info.game_components.Carpet_Level3):
                self.Carpet_Level3 = int(finish_event.level_info.game_components.Carpet_Level3)

            if str(finish_event.level_info.game_components.Chain_Level1):
                self.Chain_Level1 = int(finish_event.level_info.game_components.Chain_Level1)
            if str(finish_event.level_info.game_components.Chain_Level2):
                self.Chain_Level2 = int(finish_event.level_info.game_components.Chain_Level2)
            if str(finish_event.level_info.game_components.Chain_Level3):
                self.Chain_Level3 = int(finish_event.level_info.game_components.Chain_Level3)

            if str(finish_event.level_info.game_components.Granite_Level1):
                self.Granite_Level1 = int(finish_event.level_info.game_components.Granite_Level1)
            if str(finish_event.level_info.game_components.Granite_Level2):
                self.Granite_Level2 = int(finish_event.level_info.game_components.Granite_Level2)
            if str(finish_event.level_info.game_components.Ice_Level1):
                self.Ice_Level1 = int(finish_event.level_info.game_components.Ice_Level1)
            if str(finish_event.level_info.game_components.Ice_Level2):
                self.Ice_Level2 = int(finish_event.level_info.game_components.Ice_Level2)

            if str(finish_event.level_info.game_components.MultiStoneLevel1):
                self.MultiStoneLevel1 = int(finish_event.level_info.game_components.MultiStoneLevel1)
            if str(finish_event.level_info.game_components.MultiStoneLevel2):
                self.MultiStoneLevel2 = int(finish_event.level_info.game_components.MultiStoneLevel2)
            if str(finish_event.level_info.game_components.MultiStoneLevel3):
                self.MultiStoneLevel3 = int(finish_event.level_info.game_components.MultiStoneLevel3)

            if str(finish_event.level_info.game_components.Bear):
                self.Bear = int(finish_event.level_info.game_components.Bear)
            if str(finish_event.level_info.game_components.ChipMoves):
                self.ChipMoves = int(finish_event.level_info.game_components.ChipMoves)
            if str(finish_event.level_info.game_components.GunShot):
                self.GunShot = int(finish_event.level_info.game_components.GunShot)

            if str(finish_event.level_info.game_components.FenceDestroy):
                self.FenceDestroy = int(finish_event.level_info.game_components.FenceDestroy)
            if str(finish_event.level_info.game_components.PearlBank):
                self.PearlBank = int(finish_event.level_info.game_components.PearlBank)
            if str(finish_event.level_info.game_components.SandBank):
                self.SandBank = int(finish_event.level_info.game_components.SandBank)
            if str(finish_event.level_info.game_components.Gift):
                self.Gift = int(finish_event.level_info.game_components.Gift)

            if str(finish_event.level_info.game_components.FlowerGreen):
                self.FlowerGreen = int(finish_event.level_info.game_components.FlowerGreen)
            if str(finish_event.level_info.game_components.FlowerRed):
                self.FlowerRed = int(finish_event.level_info.game_components.FlowerRed)
            if str(finish_event.level_info.game_components.FlowerWhite):
                self.FlowerWhite = int(finish_event.level_info.game_components.FlowerWhite)
            if str(finish_event.level_info.game_components.FlowerBlack):
                self.FlowerBlack = int(finish_event.level_info.game_components.FlowerBlack)
            if str(finish_event.level_info.game_components.FlowerYellow):
                self.FlowerYellow = int(finish_event.level_info.game_components.FlowerYellow)
            if str(finish_event.level_info.game_components.FlowerBlue):
                self.FlowerBlue = int(finish_event.level_info.game_components.FlowerBlue)

        if start_event:

            level_session_id = start_event.level_session_id
            if level_session_id:
                self.level_session_id = level_session_id

            start_date = start_event.event_datetime
            if start_date:
                self.start_date = start_date
            if start_event.level_info.firstTarget:
                target1_name = start_event.level_info.firstTarget["m_type"]
                if target1_name:
                    self.target1_name = str(target1_name).replace("Color6:", "")

            if start_event.level_info.secondTarget:
                target2_name = start_event.level_info.secondTarget["m_type"]
                if target2_name:
                    self.target2_name = str(target2_name).replace("Color6:", "")
            if start_event.level_info.firstTarget:
                target1_count = start_event.level_info.firstTarget["m_required"]
                if target1_count:
                    self.target1_count = target1_count
            if start_event.level_info.secondTarget:
                target2_count = start_event.level_info.secondTarget["m_required"]
                if target2_count:
                    self.target2_count = target2_count
            first_bonus = start_event.level_info.firstBonus
            if first_bonus:
                self.first_bonus = int(first_bonus)
            second_bonus = start_event.level_info.secondBonus
            if second_bonus:
                self.second_bonus = int(second_bonus)
            third_bonus = start_event.level_info.thirdBonus
            if third_bonus:
                self.third_bonus = int(third_bonus)
            give_turn = start_event.level_info.turns
            if give_turn:
                self.give_turn = give_turn
            give_seconds = start_event.level_info.seconds
            if give_seconds:
                self.give_seconds = give_seconds

            self.user_name = start_event.level_info.userName

        if finish_event:
            if finish_event.level_info:
                self.countUseBombBonys = finish_event.level_info.countUseBombBonys

            spent_turn = int(finish_event.level_info.turns)
            if spent_turn > 0:
                self.spent_turn = spent_turn
            spent_second = int(finish_event.level_info.seconds)
            if spent_second > 0:
                self.spent_second = spent_second
            finish_date = finish_event.event_datetime
            if finish_event:
                self.end_date = finish_date
            result_game = finish_event.key_event
            if result_game:
                if result_game == "completegame":
                    self.win_game = 1
                elif result_game == "failgame":
                    self.fail_game = 1

        if lvl_end_event:
            game_currency = lvl_end_event.level_info.gameCurrency
            if game_currency or game_currency == 0:
                self.game_currency = game_currency

        if self.start_date and self.end_date:
            self.diff_time = self.end_date - self.start_date

        if self.spent_turn and self.give_turn:
            self.left_turn = self.give_turn - self.spent_turn

        # ЗАПОЛНЯЕМ ТОЛЬКО КОГДА ПОРАЖЕНИЕ
        if finish_event.level_info:
            if finish_event.level_info.firstTarget:
                if str(finish_event.level_info.firstTarget["m_required"]) and self.fail_game:
                    self.target1_count_collected = finish_event.level_info.firstTarget["m_remainder"]
            if finish_event.level_info.secondTarget:
                if str(finish_event.level_info.secondTarget["m_required"]) and self.fail_game:
                    self.target2_count_collected = finish_event.level_info.secondTarget["m_remainder"]


def get_analytic_data(level_name):
    events = get_events()

    level_events = list()
    for event in events:
        if event.level_info.levelID == level_name:
            level_events.append(event)

    finished_events = list()

    start_game_events = list()
    target_complete_events = list()
    level_complete_events = list()
    fail_game_events = list()

    for lvl_event in level_events:
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
        if fail_event is not None:
            finished_events.append(AnalyticEvenData(start_event, fail_event, None, level_name))

        else:

            complete_lvl_event = get_event_by_session_key(level_complete_events, start_event.level_session_id)
            target_event = get_event_by_session_key(target_complete_events, start_event.level_session_id)
            if complete_lvl_event is not None and target_event is not None:
                finished_events.append(AnalyticEvenData(start_event, target_event, complete_lvl_event, level_name))
            elif target_event is not None:
                finished_events.append(AnalyticEvenData(start_event, target_event, None, level_name))

    secret_keys = get_all_secret_key_in_level(finished_events)
    list_secret_key_date = list()
    for secret_key in secret_keys:
        secret_ket_data = get_total_data_by_secret_get(finished_events, secret_key)
        secret_ket_data["secret_key"] = secret_key
        list_secret_key_date.append(secret_ket_data)

    return finished_events, get_totals_data(finished_events), list_secret_key_date


def get_total_data_by_secret_get(finished_events, secret_key):
    events = list()
    for event in finished_events:
        if secret_key == event.user_name:
            events.append(event)

    return get_totals_data(events)


def get_all_secret_key_in_level(finished_events):
    secret_keys = set()
    for event in finished_events:
        secret_keys.add(event.user_name)
    return secret_keys


def get_totals_data(analytic_data):
    result_dict = dict()

    if len(analytic_data) != 0:
        class_attributes = __get_class_attributes(analytic_data[0])
        if len(class_attributes) != 0:
            for attribute in class_attributes:
                if attribute == "diff_time":
                    result_dict[attribute] = _get_diff_time(analytic_data)
                elif attribute == "level_session_id" or attribute == "start_date" or attribute == "end_date" or \
                                attribute == "target1_name" or attribute == "user_name" or attribute == "level_name":
                    pass
                elif attribute == "left_turn":
                    result_dict[attribute] = _get_data_for_left_turn(analytic_data)
                elif attribute == "fail_game" or attribute == "win_game":
                    result_dict[attribute] = _get_count_analytic_data(analytic_data, attribute)
                elif attribute == "game_currency":
                    result_dict[attribute] = _get_analytic_data_by_list_events(analytic_data, attribute) + ", " + \
                                             _get_sred_arefmetic(analytic_data, attribute)
                else:
                    result_dict[attribute] = _get_analytic_data_by_list_events(analytic_data, attribute)

    result_dict["complexity"] = _get_complexity(analytic_data)
    return result_dict


def _get_sred_arefmetic(analytic_data, attr, is_only_win=True):
    sum = 0
    count = 0

    for row in analytic_data:
        if is_only_win:
            if row.win_game == 1:
                if not str(row.game_currency).isdigit():
                    count += 1
                else:
                    sum += int(row.game_currency)
                    count += 1
        else:
            if not str(row.game_currency).isdigit():
                count += 1
            else:
                sum += int(row.game_currency)
                count += 1

    if sum == 0 or count == 0:
        return ""

    return str(sum / count)


def __get_class_attributes(cls):
    return [i for i in cls.__dict__.keys() if i[:1] != '_']


def _get_count_analytic_data(events, attr):
    full_attr_value = list()
    for row in events:
        if getattr(row, attr):
            full_attr_value.append(int(getattr(row, attr)))
    return len(full_attr_value)


def _get_complexity(events):
    fails = _get_count_analytic_data(events, "fail_game")
    all = len(events)
    wins = all - fails
    is_new_statistics = False
    date_start_new_statistics = datetime.datetime(2018, 12, 1, 0, 0)
    for event in events:
        if event.start_date:
            if event.start_date > date_start_new_statistics:
                is_new_statistics = True

    if fails != 0 and all != 0:
        percents = str(fails) + " * 100 / " + str(all) + " = " + str(
            round((fails * 100) / all, 2)) + "%"

        if wins == 0:
            tryes = str(all) + ' / ' + str(wins) + " = -"
        else:
            tryes = str(all) + ' / ' + str(wins) + " = " + \
                str(round((all / wins), 2))

        if is_new_statistics:
            return tryes
        else:
            return percents + "  |  попытка: " + tryes
    else:
        return "0"


def _get_diff_time(events):
    diff_time = list()
    for row in events:
        if row.diff_time:
            diff_time.append(row.diff_time)

    if len(events) != 0:
        delta_time = 0
        for time in diff_time:
            delta_time += time.total_seconds()
        diff_time = datetime.timedelta(seconds=(delta_time / len(events)))
        return str(diff_time)[:7]


def _get_data_for_left_turn(events):
    left_turns = list()
    for row in events:
        if row.left_turn and row.win_game:
            left_turns.append(int(row.left_turn))
    return __get_analytic_data(left_turns)


def _get_analytic_data_by_list_events(events, attr):
    full_attr_value = list()
    for row in events:
        if str(getattr(row, attr)) and str(getattr(row, attr)).isdigit():
            full_attr_value.append(int(getattr(row, attr)))
    return __get_analytic_data(full_attr_value)


def __get_analytic_data(vector):
    """ Возвращает медипну и сред. квад. если вектор не пуст, возращает сроку с прочерком"""
    if len(vector) != 0:
        return __get_median(vector) + " ± " + __get_standard_deviation(vector)
    else:
        return "-"


def __get_median(vector):
    """ медиана выборки"""
    return str(round(median(vector), 2))


def __get_standard_deviation(vector):
    """ среднеквадратическое отклонение выборки"""
    return str(round((var(vector) ** 0.5), 1))
