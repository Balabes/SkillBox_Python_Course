# -*- coding: utf-8 -*-

import simple_draw as sd
from snowfall import N, create_snowflakes, draw_snowflakes, del_snowflakes, make_move, get_fallen_snowflakes

# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall

# создать_снежинки(N)
snowflakes = []
create_snowflakes(snowflakes, N)
while True:
    draw_snowflakes(snowflakes=snowflakes, color=sd.background_color)
    make_move(snowflakes=snowflakes)
    draw_snowflakes(snowflakes=snowflakes)
    fallen = get_fallen_snowflakes(snowflakes=snowflakes)
    if len(fallen):
        draw_snowflakes(snowflakes=snowflakes, color=sd.background_color)
        del_snowflakes(snowflakes=snowflakes, death_list=fallen)
        create_snowflakes(snowflakes, len(fallen))
    sd.sleep(0.1)
    if sd.user_want_exit():
        break
    #  нарисовать_снежинки_цветом(color=sd.background_color)
    #  сдвинуть_снежинки()
    #  нарисовать_снежинки_цветом(color)
    #  если есть номера_достигших_низа_экрана() то
    #       удалить_снежинки(номера)
    #       создать_снежинки(count)

sd.pause()
