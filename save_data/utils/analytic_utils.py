from save_data.utils.events_utils import get_events
from numpy import var, median
from math import sqrt

class AnalyticEvenData:
    def __init__(self, start_event, finish_event, lvl_end_event):
        self.start_date = ""
        self.end_date = ""
        self.target1_name = ""
        self.target1_count = ""
        self.target2_name = ""
        self.target2_count = ""
        self.spent_turn = ""
        self.give_turn = ""
        self.spent_second = ""
        self.give_second = ""
        self.fail_game = ""
        self.win_game = ""
        self.spent_second = ""
        self.first_bonus = ""
        self.second_bonus = ""
        self.third_bonus = ""
        self.game_currency = ""
        self.target1_count_collected = ""
        self.target2_count_collected = ""
        self.game_currency = ""
        self.target1_count_overflow = ""
        self.target2_count_overflow = ""

        if start_event:
            start_date = start_event.event_datetime
            if start_date:
                self.start_date = start_date
            target1_name = start_event.level_info.firstTarget["m_type"]
            if target1_name:
                self.target1_name = target1_name
            target2_name = start_event.level_info.secondTarget["m_type"]
            if target2_name:
                self.target2_name = target2_name
            target1_count = start_event.level_info.firstTarget["m_required"]
            if target1_count:
                self.target1_count = target1_count
            target2_count = start_event.level_info.secondTarget["m_required"]
            if target2_count:
                self.target2_count = target2_count
            first_bonus = str(start_event.level_info.firstBonus)
            if first_bonus:
                self.first_bonus = first_bonus
            second_bonus = str(start_event.level_info.secondBonus)
            if second_bonus:
                self.second_bonus = second_bonus
            third_bonus = str(start_event.level_info.thirdBonus)
            if third_bonus:
                self.third_bonus = third_bonus
            give_turn = start_event.level_info.turns
            if give_turn:
                self.give_turn = give_turn
            give_seconds = start_event.level_info.seconds
            if give_seconds:
                self.give_second = give_seconds

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
            target1_count_collected = finish_event.level_info.firstTarget["m_remainder"]
            if target1_count_collected:
                self.target1_count_collected = target1_count_collected
            target2_count_collected = finish_event.level_info.secondTarget["m_remainder"]
            if target2_count_collected:
                self.target2_count_collected = target2_count_collected

        if lvl_end_event:
            game_currency = lvl_end_event.level_info.gameCurrency
            if game_currency:
                self.game_currency = game_currency
            target1_count_overflow = lvl_end_event.level_info.firstTarget["m_remainder"]
            if target1_count_overflow:
                self.target1_count_overflow = target1_count_overflow
            target2_count_overflow = lvl_end_event.level_info.secondTarget["m_remainder"]
            if target2_count_overflow:
                self.target2_count_overflow = target2_count_overflow


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

    for start_vent in start_game_events:
        for target_event in target_complete_events:
            for complete_event in level_complete_events:
                if start_vent.level_session_id == target_event.level_session_id == complete_event.level_session_id:
                    finished_levels.append(AnalyticEvenData(start_vent, target_event, complete_event))
        for fail_game_event in fail_game_events:
            if start_vent.level_session_id == fail_game_event.level_session_id:
                finished_levels.append(AnalyticEvenData(start_vent, fail_game_event, None))

    return finished_levels, get_totals_data(finished_levels)


def get_totals_data(analytic_data):
    wins = list()
    fails = list()
    spent_turn = list()
    spent_second = list()
    target1_count = list()
    target2_count = list()
    give_turn = list()
    give_second = list()
    target1_count_collected = list()
    target2_count_collected = list()
    target1_count_overflow = list()
    target2_count_overflow = list()
    first_bonus = list()
    second_bonus = list()
    third_bonus = list()
    game_currency = list()

    for row in analytic_data:
        if row.win_game != "":
            wins.append(1)
        if row.fail_game != "":
            fails.append(1)
        if row.spent_turn != "":
            spent_turn.append(int(row.spent_turn))
        if row.spent_second != "":
            spent_second.append(int(row.spent_second))
        if row.target1_count != "":
            target1_count.append(row.target1_count)
        if row.target2_count != "":
            target2_count.append(row.target2_count)
        if row.give_turn != "":
            give_turn.append(row.give_turn)
        if row.give_second != "":
            give_second.append(row.give_second)
        if row.target1_count_collected != "":
            target1_count_collected.append(row.target1_count_collected)
        if row.target2_count_collected != "":
            target2_count_collected.append(row.target2_count_collected)
        if row.target1_count_overflow != "":
            target1_count_overflow.append(row.target1_count_overflow)
        if row.target2_count_overflow != "":
            target2_count_overflow.append(row.target2_count_overflow)
        if row.first_bonus == "True":
            first_bonus.append(1)
        if row.second_bonus == "True":
            second_bonus.append(1)
        if row.third_bonus == "True":
            third_bonus.append(1)
        if row.game_currency.isdigit():
            game_currency.append(row.game_currency)

    result_dict = dict()
    if len(wins) != 0:
        result_dict["wins"]  = str(len(wins))
    if len(fails) != 0:
        result_dict["fails"] = str(len(fails))
    if len(spent_turn) != 0:
        result_dict["spent_turn"] = str(round(median(spent_turn), 2)) + " +-" + str(round(var(spent_turn) ** 0.5, 2))
    if len(spent_second) != 0:
        result_dict["spent_second"] = str(round(median(spent_second), 2)) + " +-" + str(round(var(spent_second) ** 0.5, 2))
    if len(target1_count) != 0:
        result_dict["target1_count"] = str(round(median(target1_count), 2)) + " +-" + str(round(var(target1_count) ** 0.5, 2))
    if len(target2_count) != 0:
        result_dict["target2_count"] = str(round(median(target2_count), 2)) + " +-" + str(round(var(target2_count) ** 0.5, 2))
    if len(give_turn) != 0:
        result_dict["give_turn"] = str(round(median(give_turn), 2)) + " +-" + str(round(var(give_turn) ** 0.5, 2))
    if len(give_second) != 0:
        result_dict["give_second"] = str(round(median(give_second), 2)) + " +-" + str(round(var(give_second) ** 0.5, 2))
    if len(target1_count_collected) != 0:
        result_dict["target1_count_collected"] = str(round(median(target1_count_collected), 2)) + " +-" + str(round(var(target1_count_collected) ** 0.5, 2))
    if len(target2_count_collected) != 0:
        result_dict["target2_count_collected"] = str(round(median(target2_count_collected), 2)) + " +-" + str(round(var(target2_count_collected) ** 0.5, 2))
    if len(target1_count_overflow) != 0:
        result_dict["target1_count_overflow"] = str(round(median(target1_count_overflow), 2)) + " +-" + str(round(var(target1_count_overflow) ** 0.5, 2))
    if len(target2_count_overflow) != 0:
        result_dict["target2_count_overflow"] = str(round(median(target2_count_overflow), 2)) + " +-" + str(round(var(target2_count_overflow) ** 0.5, 2))
    if len(first_bonus) != 0:
        result_dict["first_bonus"] = str(round(median(first_bonus), 2)) + " +-" + str(round(var(first_bonus) ** 0.5, 2))
    if len(second_bonus) != 0:
        result_dict["second_bonus"] = str(round(median(second_bonus), 2)) + " +-" + str(round(var(second_bonus) ** 0.5, 2))
    if len(third_bonus) != 0:
        result_dict["third_bonus"] = str(round(median(third_bonus), 2)) + " +-" + str(round(var(third_bonus) ** 0.5, 2))
    if len(game_currency) != 0:
        result_dict["game_currency"] = str(round(median(game_currency), 2)) + " +-" + str(round(var(game_currency) ** 0.5, 2))

    return result_dict