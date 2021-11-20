# -*- coding: utf-8 -*-

import simple_draw as sd
import random as random

sd.resolution = (1200, 800)

# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,


# можно поиграть -шрифтами- цветами и углами отклонения

# 1
# def draw_branches(start_point, _angle, _length):
#     trunk = sd.get_vector(start_point, -90, start_point.y)
#     trunk.draw()
#     delta_angle = 30
#     angle = _angle + delta_angle
#     next_point = start_point
#
#     while angle > -90:
#         br = sd.get_vector(start_point=next_point, angle=angle, length=_length)
#         next_point = br.end_point
#         angle -= delta_angle
#         br.draw()
#
#     angle = -_angle - 180 - delta_angle
#     next_point = start_point
#
#     while angle < -90:
#         br = sd.get_vector(start_point=next_point, angle=angle, length=_length)
#         next_point = br.end_point
#         angle += delta_angle
#         br.draw()

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви
# 2
# def draw_trunk(start_point):
#     trunk = sd.get_vector(start_point, -90, start_point.y)
#     trunk.draw()
#
#
# def draw_branches(start_point, angle, length):
#     if length < 10:
#         return
#
#     delta_angle = 20
#     angle_right = angle
#     angle_left = -(angle + 180)
#     next_point_right = next_point_left = start_point
#     next_length = length
#
#     brr = sd.get_vector(start_point=next_point_right, angle=angle_right, length=length)
#     next_point_right = brr.end_point
#     brr.draw()
#
#     next_length *= .65
#     next_angle = angle_right + delta_angle
#     draw_branches(start_point=next_point_right, angle=next_angle, length=next_length)
#     next_angle = angle_right - delta_angle
#     draw_branches(start_point=next_point_right, angle=next_angle, length=next_length)
#
#     brl = sd.get_vector(start_point=next_point_left, angle=angle_left, length=length)
#     next_point_left = brl.end_point
#     brl.draw()
#
#     next_length = length
#     next_length *= .65
#     next_angle = angle_left + delta_angle
#     draw_branches(start_point=next_point_left, angle=next_angle, length=next_length)
#     next_angle = angle_right - delta_angle
#     draw_branches(start_point=next_point_left, angle=next_angle, length=next_length)
#
#
# root_point = sd.get_point(600, 30)
# angle_0 = 60
# length_0 = 200
# draw_trunk(start_point=root_point)
# draw_branches(start_point=root_point, angle=angle_0, length=length_0)
# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg


# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
sd.random_number()


def draw_trunk(start_point):
    trunk = sd.get_vector(start_point, -90, start_point.y)
    trunk.draw()


def draw_branches(start_point, angle, length):
    if length < 20:
        return
    else:
        delta_angle = 30
        angle_right = angle + delta_angle
        angle_left = angle - delta_angle
        next_point_right = next_point_left = start_point

        brr = sd.get_vector(start_point=next_point_right, angle=angle_right, length=length)
        next_point_right = brr.end_point
        brr.draw()

        next_length = length * random.uniform(0.6, 0.9)
        next_angle = angle_right + delta_angle * random.uniform(0.01, 0.4)
        draw_branches(start_point=next_point_right, angle=next_angle, length=next_length)
        next_angle = angle_right - delta_angle * random.uniform(0.01, 0.4)
        draw_branches(start_point=next_point_right, angle=next_angle, length=next_length)

        brl = sd.get_vector(start_point=next_point_left, angle=angle_left, length=length)
        next_point_left = brl.end_point
        brl.draw()

        next_length = length * random.uniform(0.6, 0.9)
        next_angle = angle_left + delta_angle * random.uniform(0.01, 0.4)
        draw_branches(start_point=next_point_left, angle=next_angle, length=next_length)
        next_angle = angle_right - delta_angle * random.uniform(0.01, 0.4)
        draw_branches(start_point=next_point_left, angle=next_angle, length=next_length)


root_point = sd.get_point(600, 30)
angle_0 = 90
length_0 = 100
draw_trunk(start_point=root_point)
draw_branches(start_point=root_point, angle=angle_0, length=length_0)
print("End")
sd.pause()
