# -*- coding: utf-8 -*-

import simple_draw as sd
import random

screen_x = 1200
screen_y = 800

sd.resolution = (screen_x, screen_y)


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:
    def __init__(self):
        self.point = sd.get_point(random.randint(0, screen_x), random.randint(screen_y // 2, screen_y))
        self.size = random.randint(25, 100)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def draw(self):
        if self.point.y >= 0:
            sd.snowflake(length=self.size, center=self.point, color=self.color)

    def move(self):
        self.point.x += random.randint(-5, 5)
        self.point.y -= 10

    def can_fall(self):
        if self.point.y > 0:
            return True
        else:
            return False

    def clear_previous_picture(self):
        sd.snowflake(length=self.size, center=self.point, color=sd.background_color)


# flake = Snowflake()
#
# while True:
#     flake.clear_previous_picture()
#     flake.move()
#     flake.draw()
#     if not flake.can_fall():
#         print("Конец")
#         break
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break


def get_flakes(count=20):
    _snowflakes = []
    for _ in range(count):
        _snowflakes.append(Snowflake())
    return _snowflakes


def get_fallen_flakes():
    result = 0
    for _flake in flakes:
        if not _flake.can_fall():
            _flake.clear_previous_picture()
            flakes.remove(_flake)
            result += 1
    return result


def append_flakes(count):
    for _ in range(count):
        flakes.append(Snowflake())


# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
flakes = get_flakes(count=30)  # создать список снежинок
while True:
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
    fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
    if fallen_flakes:
        append_flakes(count=fallen_flakes)  # добавить еще сверху
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
