from save_data.utils.events_utils import get_events
from numpy import var, median
import datetime


class AnalyticEvenData:
    def __init__(self, start_event, finish_event, lvl_end_event):
        self.start_date = ""
        self.end_date = ""

        self.target1_name = ""
        self.target1_count = ""
        self.target2_name = ""
        self.target2_count = ""

        self.spent_turn = 0
        self.spent_second = 0
        self.give_turn = 0
        self.give_seconds = 0

        self.fail_game = "0"
        self.win_game = "0"

        self.first_bonus = 0
        self.second_bonus = 0
        self.third_bonus = 0

        self.game_currency = ""

        # self.target1_count_collected = ""
        # self.target2_count_collected = ""

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
        self.Super_SmallLightning_v = 0
        self.Super_SmallLightning_h = 0
        self.Super_SphereOfFire = 0

        self.Stone = 0
        self.Weight = 0
        self.Lamp = 0
        self.Balloon = 0
        self.StarBonus = 0

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

            if str(finish_event.level_info.game_components.Super_SmallLightning_v):
                self.Super_SmallLightning_v = int(finish_event.level_info.game_components.Super_SmallLightning_v)

            if str(finish_event.level_info.game_components.Super_SmallLightning_h):
                self.Super_SmallLightning_h = int(finish_event.level_info.game_components.Super_SmallLightning_h)

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

        if start_event:
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
                    self.win_game = "1"
                elif result_game == "failgame":
                    self.fail_game = "1"

        if lvl_end_event:
            game_currency = lvl_end_event.level_info.gameCurrency
            if game_currency:
                self.game_currency = game_currency
        if self.start_date and self.end_date:
            self.diff_time = self.end_date - self.start_date


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
            finished_levels.append(AnalyticEvenData(start_event, fail_event, None))
        else:
            complete_lvl_event = get_event(level_complete_events, start_event.level_session_id)
            target_event = get_event(target_complete_events, start_event.level_session_id)
            if complete_lvl_event is not None and target_event is not None:
                finished_levels.append(AnalyticEvenData(start_event, target_event, complete_lvl_event))
            elif target_event is not None:
                finished_levels.append(AnalyticEvenData(start_event, target_event, None))

    return finished_levels, get_totals_data(finished_levels)


def get_event(events, level_key):
    for event in events:
        if event.level_session_id == level_key:
            return event
    return None


def get_totals_data(analytic_data):
    result_dict = dict()
    result_dict["wins"] = _get_wins(analytic_data)
    result_dict["fails"] = _get_fails(analytic_data)
    result_dict["spent_turn"] = _get_spent_turns(analytic_data)
    result_dict["spent_second"] = _get_spent_second(analytic_data)
    result_dict["complexity"] = _get_complexity(analytic_data)
    result_dict["give_turn"] = _get_give_turns(analytic_data)
    result_dict["give_second"] = _get_give_second(analytic_data)

    # result_dict["first_bonus"] = _get_first_bonus(analytic_data)
    # result_dict["second_bonus"] = _get_second_bonus(analytic_data)
    # result_dict["third_bonus"] = _get_third_bonus(analytic_data)

    result_dict["target1_count"] = _get_target1_count(analytic_data)
    result_dict["target2_count"] = _get_target2_count(analytic_data)

    result_dict["diff_time"] = _get_diff_time(analytic_data)

    result_dict["red"] = _get_color_red(analytic_data)
    result_dict["yellow"] = _get_color_yellow(analytic_data)
    result_dict["blue"] = _get_color_blue(analytic_data)
    result_dict["green"] = _get_color_green(analytic_data)
    result_dict["white"] = _get_color_white(analytic_data)
    result_dict["black"] = _get_color_black(analytic_data)

    result_dict["Super_FireSpark"] = _get_Super_FireSpark(analytic_data)
    result_dict["Super_FireRing"] = _get_Super_FireRing(analytic_data)
    result_dict["Super_BigLightning_h"] = _get_Super_BigLightning_h(analytic_data)
    result_dict["Super_BigLightning_v"] = _get_Super_BigLightning_v(analytic_data)
    result_dict["Super_SmallLightning_v"] = _get_Super_SmallLightning_v(analytic_data)
    result_dict["Super_SmallLightning_h"] = _get_Super_SmallLightning_h(analytic_data)
    result_dict["Super_SphereOfFire"] = _get_Super_SphereOfFire(analytic_data)

    result_dict["Stone"] = _get_Stone(analytic_data)
    result_dict["Weight"] = _get_Weight(analytic_data)
    result_dict["Lamp"] = _get_Lamp(analytic_data)
    result_dict["Balloon"] = _get_Balloon(analytic_data)
    result_dict["StarBonus"] = _get_StarBonus(analytic_data)

    return result_dict


def _get_wins(events):
    wins = list()
    for row in events:
        if row.win_game == "1":
            wins.append(1)
    return str(len(wins))


def _get_fails(events):
    fails = list()
    for row in events:
        if row.fail_game == "1":
            fails.append(1)
    return str(len(fails))


def _get_spent_turns(events):
    spent_turns = list()
    for row in events:
        if row.spent_turn != "":
            spent_turns.append(int(row.spent_turn))
    return __get_analytic_data(spent_turns)


def _get_spent_second(events):
    spent_second = list()
    for row in events:
        if row.spent_second != "":
            spent_second.append(int(row.spent_second))
    return __get_analytic_data(spent_second)


def _get_complexity(events):
    fails = int(_get_fails(events))
    if fails != 0 and events != 0:
        return str(fails) + " * 100 / " + str(len(events)) + " = " + str(round((fails * 100) / len(events), 2))
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


def _get_give_turns(events):
    give_turn = list()
    for row in events:
        if row.give_turn != "":
            give_turn.append(int(row.give_turn))
    return __get_analytic_data(give_turn)


def _get_give_second(events):
    give_seconds = list()
    for row in events:
        if row.give_seconds != "":
            give_seconds.append(int(row.give_seconds))
    return __get_analytic_data(give_seconds)


def _get_first_bonus(events):
    first_bonus = list()
    for row in events:
        if bool(row.first_bonus):
            first_bonus.append(1)
    return __get_analytic_data(first_bonus)


def _get_second_bonus(events):
    second_bonus = list()
    for row in events:
        if bool(row.second_bonus):
            second_bonus.append(1)
    return __get_analytic_data(second_bonus)


def _get_third_bonus(events):
    third_bonus = list()
    for row in events:
        if bool(row.third_bonus):
            third_bonus.append(1)
    return __get_analytic_data(third_bonus)


def _get_target1_count(events):
    target1_count = list()
    for row in events:
        if row.target1_count != "":
            target1_count.append(row.target1_count)
    return __get_analytic_data(target1_count)


def _get_target2_count(events):
    target2_count = list()
    for row in events:
        if row.target2_count != "":
            target2_count.append(row.target1_count)
    return __get_analytic_data(target2_count)


def _get_color_red(events):
    color_red = list()
    for row in events:
        if str(row.red):
            color_red.append(row.red)
    print(var([1, 2, 3, 4]))
    return __get_analytic_data(color_red)


def _get_color_yellow(events):
    color_yellow = list()
    for row in events:
        if str(row.yellow):
            color_yellow.append(row.yellow)
    return __get_analytic_data(color_yellow)


def _get_color_blue(events):
    color_blue = list()
    for row in events:
        if str(row.blue):
            color_blue.append(row.blue)
    return __get_analytic_data(color_blue)


def _get_color_green(events):
    color_green = list()
    for row in events:
        if str(row.green):
            color_green.append(row.green)
    return __get_analytic_data(color_green)


def _get_color_white(events):
    color_white = list()
    for row in events:
        if str(row.white):
            color_white.append(row.white)
    return __get_analytic_data(color_white)


def _get_color_black(events):
    color_black = list()
    for row in events:
        if str(row.black):
            color_black.append(row.black)
    return __get_analytic_data(color_black)


def _get_Super_FireSpark(events):
    super_FireSpark = list()
    for row in events:
        if str(row.Super_FireSpark):
            super_FireSpark.append(row.Super_FireSpark)
    return __get_analytic_data(super_FireSpark)


def _get_Super_FireRing(events):
    Super_FireRing = list()
    for row in events:
        if str(row.Super_FireRing):
            Super_FireRing.append(row.Super_FireRing)
    return __get_analytic_data(Super_FireRing)


def _get_Super_BigLightning_h(events):
    Super_BigLightning_h = list()
    for row in events:
        if str(row.Super_BigLightning_h):
            Super_BigLightning_h.append(row.Super_BigLightning_h)
    return __get_analytic_data(Super_BigLightning_h)


def _get_Super_BigLightning_v(events):
    Super_BigLightning_v = list()
    for row in events:
        if str(row.Super_BigLightning_v):
            Super_BigLightning_v.append(row.Super_BigLightning_v)
    return __get_analytic_data(Super_BigLightning_v)


def _get_Super_SmallLightning_v(events):
    Super_SmallLightning_v = list()
    for row in events:
        if str(row.Super_SmallLightning_v):
            Super_SmallLightning_v.append(row.Super_SmallLightning_v)
    return __get_analytic_data(Super_SmallLightning_v)


def _get_Super_SmallLightning_h(events):
    Super_SmallLightning_h = list()
    for row in events:
        if str(row.Super_SmallLightning_h):
            Super_SmallLightning_h.append(row.Super_SmallLightning_h)
    return __get_analytic_data(Super_SmallLightning_h)


def _get_Super_SphereOfFire(events):
    Super_SphereOfFire = list()
    for row in events:
        if str(row.Super_SphereOfFire):
            Super_SphereOfFire.append(row.Super_SphereOfFire)
    return __get_analytic_data(Super_SphereOfFire)


def _get_Stone(events):
    Stone = list()
    for row in events:
        if str(row.Stone):
            Stone.append(row.Stone)
    return __get_analytic_data(Stone)


def _get_Weight(events):
    Weight = list()
    for row in events:
        if str(row.Weight):
            Weight.append(row.Weight)
    return __get_analytic_data(Weight)


def _get_Lamp(events):
    Lamp = list()
    for row in events:
        if str(row.Lamp):
            Lamp.append(row.Lamp)
    return __get_analytic_data(Lamp)


def _get_Balloon(events):
    Balloon = list()
    for row in events:
        if str(row.Balloon):
            Balloon.append(row.Balloon)
    return __get_analytic_data(Balloon)


def _get_StarBonus(events):
    StarBonus = list()
    for row in events:
        if str(row.StarBonus):
            StarBonus.append(row.StarBonus)
    return __get_analytic_data(StarBonus)


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
    return str(round(var(vector) ** 0.5, 4))
