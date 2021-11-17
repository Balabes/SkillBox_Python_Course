# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.
sd.resolution = (700, 700)


def draw_smile(x, y, color):
    """Ебать серьезный"""
    center_point = sd.get_point(x, y)
    sd.circle(center_point, 100, color, 2)
    left_eye = sd.get_point(x - 50, y + 60)
    sd.circle(left_eye, 10, color, 2)
    right_eye = sd.get_point(x + 50, y + 60)
    sd.circle(right_eye, 10, color, 2)
    nose_start = sd.get_point(x, y + 50)
    nose_stop = sd.get_point(x, y + 10)
    sd.line(nose_start, nose_stop, color, 2)
    mouth_start = sd.get_point(x - 40, y - 50)
    mouth_stop = sd.get_point(x + 40, y - 50)
    sd.line(mouth_start, mouth_stop, color, 2)


for _ in range(10):
    point = sd.random_point()
    draw_smile(point.x, point.y, sd.COLOR_ORANGE)

sd.pause()
