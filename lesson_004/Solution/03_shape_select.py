# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 800)


# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg
def draw_figure_side(_start_point, _angle, _length, _color):
    side = sd.get_vector(start_point=_start_point, angle=_angle, length=_length, width=1)
    side.draw(color=_color)
    return side.end_point


def draw_triangle2(_point, _angle, _len, _color):
    next_point = _point
    for _i in range(3):
        next_point = draw_figure_side(_start_point=next_point, _angle=_angle - 360 / 3 * _i, _length=_len,
                                      _color=_color)


def draw_square2(_point, _angle, _len, _color):
    next_point = _point
    for _i in range(4):
        next_point = draw_figure_side(_start_point=next_point, _angle=_angle - 360 / 4 * _i, _length=_len,
                                      _color=_color)


def draw_pentagon2(_point, _angle, _len, _color):
    next_point = _point
    for _i in range(5):
        next_point = draw_figure_side(_start_point=next_point, _angle=_angle - 360 / 5 * _i, _length=_len,
                                      _color=_color)


def draw_hexagon2(_point, _angle, _len, _color):
    next_point = _point
    for _i in range(6):
        next_point = draw_figure_side(_start_point=next_point, _angle=_angle - 360 / 6 * _i, _length=_len,
                                      _color=_color)


point = sd.get_point(600, 500)
angle = 0
length = 200
color = sd.COLOR_WHITE
shapes = {1: "Треугольник", 2: "Квадрат", 3: "Пятиугольник", 4: "Шестиугольник"}
print("Выбери фигуру!")
for i, item in shapes.items():
    print(f"{i}. {item}")

shape_select = int(input())
print(shape_select)

if not (1 <= shape_select <= 4):
    print("Fuck you! Нужно выбрать 1-4")
else:
    print(f"Ты выбрал {shapes[shape_select]}")
    if shape_select == 1:
        draw_triangle2(_point=point, _angle=angle, _len=length, _color=color)
    if shape_select == 2:
        draw_square2(_point=point, _angle=angle, _len=length, _color=color)
    if shape_select == 3:
        draw_pentagon2(_point=point, _angle=angle, _len=length, _color=color)
    if shape_select == 4:
        draw_hexagon2(_point=point, _angle=angle, _len=length, _color=color)

sd.pause()
