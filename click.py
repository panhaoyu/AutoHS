import win32gui
import win32api
import win32con
import time
from pynput.mouse import Button, Controller
import random

OPERATE_INTERVAL = 0.2
SMALL_OPERATE_INTERVAL = 0.1


def choose_my_minion(mine_index, mine_num):
    time.sleep(OPERATE_INTERVAL)
    x = 960 - (mine_num - 1) * 70 + mine_index * 140
    y = 600
    left_click(x, y)


def choose_opponent_minion(oppo_index, oppo_num):
    time.sleep(OPERATE_INTERVAL)
    x = 960 - (oppo_num - 1) * 70 + oppo_index * 140
    y = 400
    left_click(x, y)


def choose_oppo_hero():
    time.sleep(OPERATE_INTERVAL)
    left_click(960, 200)


def cancel_click():
    time.sleep(SMALL_OPERATE_INTERVAL)
    right_click(50, 400)


def left_click(x, y):
    x += random.randint(-5, 5)
    y += random.randint(-5, 5)
    mouse = Controller()
    time.sleep(0.2)
    mouse.position = (x, y)
    time.sleep(0.2)
    mouse.press(Button.left)
    time.sleep(0.2)
    mouse.release(Button.left)


def right_click(x, y):
    x += random.randint(-5, 5)
    y += random.randint(-5, 5)
    mouse = Controller()
    time.sleep(0.2)
    mouse.position = (x, y)
    time.sleep(0.2)
    mouse.press(Button.right)
    time.sleep(0.2)
    mouse.release(Button.right)


def match_opponent():
    left_click(1400, 900)


def end_turn():
    left_click(1550, 500)


def choose_card():
    left_click(950, 500)
    left_click(960, 860)


def emoj():
    emoj_list = [(800, 780), (1140, 780), (800, 680), (1150, 680)]
    right_click(950, 830)
    time.sleep(OPERATE_INTERVAL)
    x, y = emoj_list[random.randint(0, 3)]
    left_click(x, y)
    time.sleep(OPERATE_INTERVAL)


def use_card():
    card_list = [(700, 1060), (800, 1060), (880, 1060), (950, 1060), (1050, 1060), (1150, 1060)]
    card_list.reverse()
    for coor_tuple in card_list:
        left_click(coor_tuple[0], coor_tuple[1])
        time.sleep(OPERATE_INTERVAL)
        left_click(950, 200)


def use_skill():
    left_click(1150, 850)


# TODO: delete it
def minion_attack():
    for minion_location in range(800, 1101, 100):
        left_click(minion_location, 600)
        time.sleep(OPERATE_INTERVAL)
        left_click(950, 200)
    right_click(50, 400)


def minion_beat_minion(mine_index, mine_number, oppo_index, oppo_num):
    choose_my_minion(mine_index, mine_number)
    choose_opponent_minion(oppo_index, oppo_num)
    cancel_click()


def minion_beat_hero(mine_index, mine_number):
    choose_my_minion(mine_index, mine_number)
    choose_oppo_hero()
    cancel_click()


def hero_attack():
    left_click(950, 830)
    time.sleep(OPERATE_INTERVAL)
    left_click(950, 200)
    cancel_click()


def use_task():
    left_click(700, 1000)
    time.sleep(OPERATE_INTERVAL)
    left_click(950, 200)


def enter_HS():
    left_click(350, 970)


def enter_battle_mode():
    left_click(950, 320)


if __name__ == "__main__":
    left_click(350, 970)
