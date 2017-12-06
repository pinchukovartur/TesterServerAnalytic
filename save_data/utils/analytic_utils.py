from save_data.utils.events_utils import get_events
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

        self.Box_Level1 = 0
        self.Box_Level2 = 0
        self.Box_Level3 = 0

        self.Carpet_Level1 = 0
        self.Carpet_Level2 = 0
        self.Carpet_Level3 = 0

        self.Chain_Level1 = 0
        self.Chain_Level2 = 0
        self.Chain_Level3 = 0

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
                    self.target1_name = target1_name

            if start_event.level_info.secondTarget:
                target2_name = start_event.level_info.secondTarget["m_type"]
                if target2_name:
                    self.target2_name = target2_name
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
            if game_currency:
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

    finished_levels = list()

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

        fail_event = get_event(fail_game_events, start_event.level_session_id)
        if fail_event is not None:
            finished_levels.append(AnalyticEvenData(start_event, fail_event, None, level_name))

        else:

            complete_lvl_event = get_event(level_complete_events, start_event.level_session_id)
            target_event = get_event(target_complete_events, start_event.level_session_id)
            if complete_lvl_event is not None and target_event is not None:
                finished_levels.append(AnalyticEvenData(start_event, target_event, complete_lvl_event, level_name))
            elif target_event is not None:
                finished_levels.append(AnalyticEvenData(start_event, target_event, None, level_name))
    return finished_levels, get_totals_data(finished_levels)


def get_event(events, level_key):
    for event in events:
        if event.level_session_id == level_key:
            return event
    return None


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
                else:
                    result_dict[attribute] = _get_analytic_data_by_list_events(analytic_data, attribute)

    result_dict["complexity"] = _get_complexity(analytic_data)

    return result_dict


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

    if fails != 0 and events != 0:
        return str(fails) + " * 100 / " + str(len(events)) + " = " + str(
            round(((fails) * 100) / len(events), 2))
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
