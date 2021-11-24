# -*- coding: utf-8 -*-

# Создать пакет, в который скопировать функции отрисовки из предыдущего урока
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# пример см. lesson_005/results/04_painting.jpg
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)

import simple_draw as sd
import draw.wall as wall
import draw.roof as roof
import draw.sun as sun
import draw.tree as tree
import draw.rainbow as rainbow
import draw.smile as smile
import draw.snow as snow

sd.resolution = (1400, 800)


wall.draw_wall(x_start=400, y_start=10, x_stop=800, y_stop=410)
point = roof.draw_roof(400, 410, 800 - 400)
sun.draw_sun(100, 600, 100)
tree.draw_tree(1200, 100)
rainbow.draw_rainbow(rainbow.rainbow_colors, 700, 0, 750, 10)
smile.draw_smile(point.x, point.y + 100, color=sd.COLOR_ORANGE)
snow.snowflakes_init()
snow.snowflake_fall(snow.snowflakes_list)

sd.pause()
# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.
