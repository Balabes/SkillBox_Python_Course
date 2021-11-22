# -*- coding: utf-8 -*-

# Создать модуль my_burger. В нем определить функции добавления инградиентов:
#  - булочки
#  - котлеты
#  - огурчика
#  - помидорчика
#  - майонеза
#  - сыра
# В каждой функции выводить на консоль что-то вроде "А теперь добавим ..."

# В этом модуле создать рецепт двойного чизбургера (https://goo.gl/zA3goZ)
# с помощью фукций из my_burger и вывести на консоль.

# Создать рецепт своего бургера, по вашему вкусу.
# Если не хватает инградиентов - создать соответствующие функции в модуле my_burger

import my_burger as ingredients


def do_double_cheeseburger():
    print("Double cheeseburger")
    ingredients.add_bun()
    ingredients.add_ketchup()
    ingredients.add_steak()
    ingredients.add_cheese()
    ingredients.add_steak()
    ingredients.add_cheese()
    ingredients.add_onion()
    ingredients.add_pickle()
    ingredients.add_ketchup()
    ingredients.add_mustard()
    ingredients.add_bun()


def do_my_burger():
    print("My burger")
    ingredients.add_bun()
    ingredients.add_ketchup()
    ingredients.add_mustard()
    ingredients.add_mayo()
    ingredients.add_salad()
    ingredients.add_steak()
    ingredients.add_cheese()
    ingredients.add_bacon()
    ingredients.add_fried_onion()
    ingredients.add_pickle()
    ingredients.add_tomato()
    ingredients.add_bun()


do_double_cheeseburger()
do_my_burger()
