# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1600, 950)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
radius = 50
center_point = sd.get_point(100, 870)
for _ in range(3):
    sd.circle(center_point, radius, (255, 255, 255), 2)
    radius += 5


# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг


def draw_bubble(null_point, step):
    radius = 50
    for _ in range(3):
        radius += step
        sd.circle(null_point, radius, (255, 255, 255), 2)


point = sd.get_point(100, 750)
draw_bubble(point, step=5)

# Нарисовать 10 пузырьков в ряд
for x in range(100, 1501, 150):
    point = sd.get_point(x, 620)
    draw_bubble(point, 5)

# Нарисовать три ряда по 10 пузырьков
for y in range(200, 500, 120):
    for x in range(100, 1501, 150):
        point = sd.get_point(x, y)
        draw_bubble(point, 5)
# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for _ in range(100):
    random_point = sd.random_point()
    draw_bubble(random_point, 5)

sd.pause()
