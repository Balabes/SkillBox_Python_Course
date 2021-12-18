# -*- coding: utf-8 -*-

import simple_draw as sd


# На основе вашего кода из решения lesson_004/01_shapes.py сделать функцию-фабрику,
# которая возвращает функции рисования треугольника, четырехугольника, пятиугольника и т.д.
#
# Функция рисования должна принимать параметры
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Функция-фабрика должна принимать параметр n - количество сторон.


def get_polygon(n):
    def draw_shape(start_point, angle, length):
        next_point = start_point
        for i in range(n):
            side = sd.get_vector(start_point=next_point, angle=angle - 360 / n * i, length=length, width=1)
            side.draw()
            next_point = side.end_point

    return draw_shape


draw_triangle = get_polygon(n=3)
draw_triangle(start_point=sd.get_point(200, 200), angle=13, length=100)

draw_4 = get_polygon(4)
draw_4(start_point=sd.get_point(400, 200), angle=90, length=100)

sd.pause()
