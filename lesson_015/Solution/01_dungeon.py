# -*- coding: utf-8 -*-

# С помощью JSON файла rpg.json задана "карта" подземелья.
# Подземелье было выкопано монстрами и они всё ещё скрываются где-то в его глубинах,
# планируя набеги на близлежащие поселения.
# Само подземелье состоит из двух главных разветвлений и нескольких развилок,
# и лишь один из путей приведёт вас к главному Боссу
# и позволит предотвратить набеги и спасти мирных жителей.

# Напишите игру, в которой пользователь, с помощью консоли,
# сможет:
# 1) исследовать это подземелье:
#   -- передвижение должно осуществляться присваиванием переменной и только в одну сторону
#   -- перемещаясь из одной локации в другую, пользователь теряет время, указанное в конце названия каждой локации
# Так, перейдя в локацию Location_1_tm500 - вам необходимо будет списать со счёта 500 секунд.
# Тег, в названии локации, указывающий на время - 'tm'.
#
# 2) сражаться с монстрами:
#   -- сражение имитируется списанием со счета персонажа N-количества времени и получением N-количества опыта
#   -- опыт и время указаны в названиях монстров (после exp указано значение опыта и после tm указано время)
# Так, если в локации вы обнаружили монстра Mob_exp10_tm20 (или Boss_exp10_tm20)
# необходимо списать со счета 20 секунд и добавить 10 очков опыта.
# Теги указывающие на опыт и время - 'exp' и 'tm'.
# После того, как игра будет готова, сыграйте в неё и наберите 280 очков при положительном остатке времени.

# По мере продвижения вам так же необходимо вести журнал,
# в котором должна содержаться следующая информация:
# -- текущее положение
# -- текущее количество опыта
# -- текущая дата (отсчёт вести с первой локации с помощью datetime)
# После прохождения лабиринта, набора 280 очков опыта и проверки на остаток времени (remaining_time > 0),
# журнал необходимо записать в csv файл (назвать dungeon.csv, названия столбцов взять из field_names).

# Пример лога игры:
# Вы находитесь в Location_0_tm0
# У вас 0 опыта и осталось 1234567890.0987654321 секунд
# Прошло уже 0:00:00
# Внутри вы видите:
# -- Монстра Mob_exp10_tm0
# -- Вход в локацию: Location_1_tm10400000
# -- Вход в локацию: Location_2_tm333000000
# Выберите действие:
# 1.Атаковать монстра
# 2.Перейти в другую локацию
# 3.Выход

remaining_time = '1234567890.0987654321'
# если изначально не писать число в виде строки - теряется точность!
field_names = ['current_location', 'current_experience', 'current_date']
# Учитывая время и опыт, не забывайте о точности вычислений!

from select import select
import datetime
import json
import os
import re
import time
import csv
from decimal import *
from pprint import pprint


class Game:
    def __init__(self):
        self._dungeon_file = "rpg.json"
        with open(self._dungeon_file, "r") as read_file:
            self.dungeon = json.load(read_file)
        self.remaining_time_str = '1234567890.0987654321'
        getcontext().prec = 50
        self.remaining_time = Decimal(self.remaining_time_str)
        self.exp = Decimal(0)
        self.start_time = time.monotonic()
        self.cur_location = "Location_0_tm0"
        self.prev_location = ""
        # for item in self.dungeon[self.cur_location]:
        #     if isinstance(item, dict):
        #         pprint(list(item)[0])
        #     else:
        #         pprint(item)

    def print_user_interface(self):
        print(f"Вы находитесь в {self.cur_location}")
        print(f"У вас {self.exp} опыта и осталось {self.remaining_time} секунд")
        elapsed_time = time.monotonic() - self.start_time
        print(f"Прошло уже {elapsed_time}")
        print(f"Внутри вы видите:")
        for item in self.dungeon[self.cur_location]:
            if isinstance(item, dict):
                print(f"Вход в локацию {list(item)[0]}")
            else:
                print(f"Монстра {item}")


g = Game()
g.print_user_interface()