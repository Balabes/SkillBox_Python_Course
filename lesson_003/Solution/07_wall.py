# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
sd.resolution = (700, 700)

y = -50
x = -100
brick_height = 50
brick_width = 100
for i in range(14):
    y += brick_height
    start_point = sd.get_point(0, y)
    stop_point = sd.get_point(700, y)
    sd.line(start_point, stop_point, sd.COLOR_YELLOW, 1)
    if i % 2 == 0:
        x = -100
        for _ in range(7):
            x += brick_width
            start_point = sd.get_point(x, y)
            stop_point = sd.get_point(x, y + brick_height)
            sd.line(start_point, stop_point, sd.COLOR_YELLOW, 1)
    if i % 2 != 0:
        x = -50
        for _ in range(7):
            x += brick_width
            start_point = sd.get_point(x, y)
            stop_point = sd.get_point(x, y + brick_height)
            sd.line(start_point, stop_point, sd.COLOR_YELLOW, 1)

sd.pause()
