import random
import numpy as np
import matplotlib.pyplot as plt
import math

def roll():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die2 + die1
# ставка
# рол
# подсчет
def bet(i):
    print("bet")

average_winings = []

def round():
    bet = 1
    # ставка
    single_roll = roll()
    if single_roll ==7:  # выигрыш 4:1
        return 1
    else:
        return -1

EV_UNIT = 0
average_winnings = []
round_history = []
list_intervals_down = []
list_intervals_up = []
mat_ojidanie = 0
EV_per_Unit = 0
game_outcomes = [0, 0, 0]
experiment = 1000000
win_chance = 0

def game():
    global EV_per_Unit
    bet = 1
    win = 0
    capital = 1
    game_number = 0
    game_length = 0
    overall_length = 0
    winnings = 0  # Ожидаемый выигрыш/проигрыш если - то казино в плюсе на эти деньги
    for i in range(1, experiment + 1):
        game_length += 1
        if capital == 0:
            game_number += 1
            capital = 1
            overall_length += game_length
            game_length = 0
        lets_play = round()
        if lets_play == 1:
            round_history.append(bet*4)
            win += 1
            winnings += bet*4
            capital += bet*4
        if lets_play == -1:
            round_history.append(-1)
            winnings -= bet
            capital -= bet
        average_winnings.append(winnings / (i * bet))

    # Построение дов. вероятности
    disp = np.var(round_history)
    for i in range(0, len(round_history) - 1):
        list_intervals_down.append(average_winnings[i + 1] - (1.65 / math.sqrt(i + 1)) * disp)
        list_intervals_up.append(average_winnings[i + 1] + (1.65 / math.sqrt(i + 1)) * disp)

    # Вывод результатов
    win_chance = win / experiment
    print("Chance to win " + str(win_chance))
    print("Expected Value " + str(winnings))  # Ожидаемый выигрыш/проигрыш если - то казино в плюсе на эти деньги
    EV_per_Unit = winnings / (experiment * bet)
    print("EV per Unit " + str(EV_per_Unit))  # Ожидаемый выигрыш/проигрыш на одну ставку
    House_Edge = EV_per_Unit * 100
    print("House Edge " + str(House_Edge))  # Преимущество /доход заведения (house advantage/house edge, H.A.)
    RTP = 1 + winnings / (experiment * bet)
    print("Return to Player " + str(RTP))  # Процент возврата (Return To Player, RTP)
    EV_per_Unit_Squared = EV_per_Unit ** 2
    EV_per_Squared_Unit = (win / experiment) + ((experiment - win) / experiment)
    VAR = EV_per_Squared_Unit - EV_per_Unit_Squared  # Дисперсия - возможно

    print("Variance " + str(np.var(round_history)))
    Standart_Deviation = VAR ** 0.5
    print("Standard deviation " + str(Standart_Deviation))
    EV_Units = EV_per_Unit * experiment
    SD_Units = Standart_Deviation * (experiment ** 0.5)
    print("Average total win " + str(EV_Units) + "\n"
          + "Its standard deviation " + str(SD_Units))

    z = 1.65
    VI = z * Standart_Deviation
    confidence_interval_low = RTP - VI / math.sqrt(experiment)
    confidence_interval_up = RTP + VI / math.sqrt(experiment)

    print("Lower confidence interval " + str(confidence_interval_low))
    print("Upper confidence interval " + str(confidence_interval_up))
    print("Game volatility index " + str(VI))
    print("Average game length " + str(overall_length / game_number))


# def build_graphic():
#     # -------график доверительной вероятности----
#     # plt.title("График доверительной вероятности")
#     # plt.hlines(EV_per_Unit, 0, 10000000)
#     # plt.plot(list_intervals_down)
#     # plt.plot(list_intervals_up)
#     # plt.ylim(-0.2, 0.2)
#     # plt.xlim(0, 10000000)
#
#     # # -------график средних выигрышей--------
#     # plt.plot(average_winnings)
#     # plt.title("График средних выигрышей")
#     # # медиана
#     # plt.hlines(np.median(average_winnings), 0, experiment, colors='r', label='Медиана')
#     # # график стремится к мат ожиданию
#     # a = np.std(average_winnings)
#     # plt.hlines(a, 0, experiment, colors='yellow', label='Ско')
#     # plt.hlines(-a, 0, experiment, colors='yellow', label='-Ско')
#     # plt.ylim(-0.4, 0.1)
#     # plt.xlim(0, 100000)
#     # plt.legend()
#     # plt.show()
#
#     # -------график распределения выигрышей---------
#     plt.title("График распределения выигрышей")
#     plt.vlines(4, 0, 0.16)
#     plt.vlines(-1, 0, 0.84)
#     plt.legend()
#     plt.show()

if __name__ == '__main__':
    game()
    # build_graphic()

