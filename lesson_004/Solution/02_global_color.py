# -*- coding: utf-8 -*-
import simple_draw as sd

sd.resolution = (1200, 600)
# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

colors = {1: sd.COLOR_RED, 2: sd.COLOR_ORANGE, 3: sd.COLOR_YELLOW, 4: sd.COLOR_GREEN, 5: sd.COLOR_CYAN,
          6: sd.COLOR_BLUE, 7: sd.COLOR_PURPLE}
colors_list = {1: 'Красный', 2: 'Оранжевый', 3: 'Желтый', 4: 'Зеленый', 5: 'Сине-зелёный',
               6: 'Синий', 7: 'Пурпурный'}


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


print("Выбери цвет!")
for i, item in colors_list.items():
    print(f"{i}. {item}")

color_select = int(input())
print(color_select)

if not (1 <= color_select <= 7):
    print("Fuck you! Нужно выбрать 1-7")
else:
    print(f"Ты выбрал {colors_list[color_select]} - {colors[color_select]}")
    x = 100
    y = 300
    start_point = sd.get_point(x, y)
    angle = 0
    length = 100
    draw_triangle2(_point=start_point, _angle=angle, _len=length, _color=colors[color_select])
    x += 200
    start_point = sd.get_point(x, y)
    draw_square2(_point=start_point, _angle=angle, _len=length, _color=colors[color_select])
    x += 200
    start_point = sd.get_point(x, y)
    draw_pentagon2(_point=start_point, _angle=angle, _len=length, _color=colors[color_select])
    x += 200
    start_point = sd.get_point(x, y)
    draw_hexagon2(_point=start_point, _angle=angle, _len=length, _color=colors[color_select])

sd.pause()
