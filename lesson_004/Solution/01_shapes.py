# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1000, 1000)
# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg
point_null = sd.get_point(500, 500)
angle = 90
length = 100


# def draw_triangle(_point, _angle, _len):
#     v1 = sd.get_vector(start_point=_point, angle=_angle - 360 / 3 * 0, length=_len, width=5)
#     v1.draw()
#     v2 = sd.get_vector(start_point=v1.end_point, angle=_angle - 360 / 3 * 1, length=_len, width=5)
#     v2.draw()
#     v3 = sd.get_vector(start_point=v2.end_point, angle=_angle - 360 / 3 * 2, length=_len, width=5)
#     v3.draw()
#
#
# draw_triangle(point_null, angle, length)
#
#
# def draw_square(_point, _angle, _len):
#     v1 = sd.get_vector(start_point=_point, angle=_angle - 360 / 4 * 0, length=_len, width=5)
#     v1.draw()
#     v2 = sd.get_vector(start_point=v1.end_point, angle=_angle - 360 / 4 * 1, length=_len, width=5)
#     v2.draw()
#     v3 = sd.get_vector(start_point=v2.end_point, angle=_angle - 360 / 4 * 2, length=_len, width=5)
#     v3.draw()
#     v4 = sd.get_vector(start_point=v3.end_point, angle=_angle - 360 / 4 * 3, length=_len, width=5)
#     v4.draw()
#
#
# point_null = sd.get_point(200, 200)
# draw_square(_point=point_null, _angle=angle, _len=length)
#
#
# def draw_pentagon(_point, _angle, _len):
#     v1 = sd.get_vector(start_point=_point, angle=_angle - 360 / 5 * 0, length=_len, width=5)
#     v1.draw()
#     v2 = sd.get_vector(start_point=v1.end_point, angle=_angle - 360 / 5 * 1, length=_len, width=5)
#     v2.draw()
#     v3 = sd.get_vector(start_point=v2.end_point, angle=_angle - 360 / 5 * 2, length=_len, width=5)
#     v3.draw()
#     v4 = sd.get_vector(start_point=v3.end_point, angle=_angle - 360 / 5 * 3, length=_len, width=5)
#     v4.draw()
#     v5 = sd.get_vector(start_point=v4.end_point, angle=_angle - 360 / 5 * 4, length=_len, width=5)
#     v5.draw()
#
#
# point_null = sd.get_point(200, 400)
# draw_pentagon(_point=point_null, _angle=angle, _len=length)
#
#
# def draw_hexagon(_point, _angle, _len):
#     v1 = sd.get_vector(start_point=_point, angle=_angle - 360 / 6 * 0, length=_len, width=5)
#     v1.draw()
#     v2 = sd.get_vector(start_point=v1.end_point, angle=_angle - 360 / 6 * 1, length=_len, width=5)
#     v2.draw()
#     v3 = sd.get_vector(start_point=v2.end_point, angle=_angle - 360 / 6 * 2, length=_len, width=5)
#     v3.draw()
#     v4 = sd.get_vector(start_point=v3.end_point, angle=_angle - 360 / 6 * 3, length=_len, width=5)
#     v4.draw()
#     v5 = sd.get_vector(start_point=v4.end_point, angle=_angle - 360 / 6 * 4, length=_len, width=5)
#     v5.draw()
#     v6 = sd.get_vector(start_point=v5.end_point, angle=_angle - 360 / 6 * 5, length=_len, width=5)
#     v6.draw()
#
#
# point_null = sd.get_point(200, 600)
# draw_hexagon(_point=point_null, _angle=angle, _len=length)


# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!

def draw_figure_side(_start_point, _angle, _length):
    side = sd.get_vector(start_point=_start_point, angle=_angle, length=_length, width=1)
    side.draw()
    # end_point = sd.get_point(side.end_point.x-1, side.end_point.y-1)
    return side.end_point


def draw_triangle2(_point, _angle, _len):
    next_point = _point
    for i in range(3):
        next_point = draw_figure_side(_start_point=next_point, _angle=_angle - 360 / 3 * i, _length=_len)


draw_triangle2(point_null, angle, length)


def draw_square2(_point, _angle, _len):
    next_point = _point
    for i in range(4):
        next_point = draw_figure_side(_start_point=next_point, _angle=_angle - 360 / 4 * i, _length=_len)


point_null = sd.get_point(200, 200)
draw_square2(_point=point_null, _angle=angle, _len=length)


def draw_pentagon2(_point, _angle, _len):
    next_point = _point
    for i in range(5):
        next_point = draw_figure_side(_start_point=next_point, _angle=_angle - 360 / 5 * i, _length=_len)


point_null = sd.get_point(200, 400)
draw_pentagon2(_point=point_null, _angle=angle, _len=length)


def draw_hexagon2(_point, _angle, _len):
    next_point = _point
    for i in range(6):
        next_point = draw_figure_side(_start_point=next_point, _angle=_angle - 360 / 6 * i, _length=_len)


point_null = sd.get_point(200, 600)
draw_hexagon2(_point=point_null, _angle=angle, _len=length)



sd.pause()
