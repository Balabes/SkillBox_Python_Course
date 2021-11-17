# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
sd.resolution = (700, 700)
# x = 45
# step = 5
# width = 4
# for color in rainbow_colors:
#     x += step
#     start_point = sd.get_point(x, 50)
#     stop_point = sd.get_point(x + 350, 450)
#     sd.line(start_point, stop_point, color, width)

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
radius = 90
step = 10
for color in rainbow_colors:
    radius += step
    start_point = sd.get_point(350, 0)
    sd.circle(start_point, radius, color, 10)

sd.pause()
