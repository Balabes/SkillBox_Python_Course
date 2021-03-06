# -*- coding: utf-8 -*-

# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.

# -*- coding: utf-8 -*-

from random import randint

# Реализуем модель человека.
# Человек может есть, работать, играть, ходить в магазин.
# У человека есть степень сытости, немного еды и денег.
# Если сытость < 0 единиц, человек умирает.
# Человеку надо прожить 365 дней.
from termcolor import cprint


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return "Я - {}, сытость {}. ".format(self.name, self.fullness)

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='blue')
            self.fullness += 10
            self.house.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='blue')

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10

    def watch_mtv(self):
        cprint('{} смотрел MTV целый день'.format(self.name), color='blue')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='blue')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='blue')

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} Вьехал в дом'.format(self.name), color='blue')

    def get_cat(self, cat):
        cat.house = self.house
        cprint('{} взял кота {}'.format(self.name, cat.nickname), color='blue')

    def buy_cat_food(self):
        self.house.cat_food += 50
        self.house.money -= 50
        cprint('{} купил кошачьей еды'.format(self.name), color='blue')

    def clean_house(self):
        self.house.dirt -= 100
        self.fullness -= 20
        cprint('{} убрался дома'.format(self.name), color='blue')

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness <= 20:
            self.eat()
        elif self.house.food < 10:
            self.shopping()
        elif self.house.money < 50:
            self.work()
        elif self.house.cat_food < 10:
            self.buy_cat_food()
        elif self.house.dirt > 100:
            self.clean_house()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_mtv()


class House:

    def __init__(self):
        self.food = 50
        self.money = 0
        self.cat_food = 0
        self.dirt = 0

    def __str__(self):
        return 'В доме еды осталось {}, кошачьего корма {}, денег осталось {}, грязь {}'.format(
            self.food, self.cat_food, self.money, self.dirt)


class Cat:
    def __init__(self, nickname):
        self.nickname = nickname
        self.hungry = 50
        self.house = None

    def __str__(self):
        return "Я кот - {}, сытость {}. ".format(self.nickname, self.hungry)

    def eat(self):
        if self.house.cat_food >= 10:
            cprint('Кот {} поел'.format(self.nickname), color='yellow')
            self.hungry += 20
            self.house.cat_food -= 10
        else:
            self.hungry -= 10
            cprint('{} нет еды'.format(self.nickname), color='yellow')

    def scratching_wallpaper(self):
        self.hungry -= 10
        self.house.dirt += 5
        cprint('{} дерет обои'.format(self.nickname), color='yellow')

    def sleep(self):
        self.hungry -= 10
        cprint('{} спит'.format(self.nickname), color='yellow')

    def act(self):
        if self.hungry <= 0:
            cprint('{} умер...'.format(self.nickname), color='red')
            return
        dice = randint(1, 6)
        if self.hungry < 30:
            self.eat()
        elif dice == 1:
            self.scratching_wallpaper()
        elif dice == 2:
            self.eat()
        else:
            self.sleep()


man = Man(name="Джон")
cat = Cat(nickname="Гарфилд")
home = House()

man.go_to_the_house(house=home)
man.get_cat(cat=cat)

for day in range(1, 366):
    print('================ день {} =================='.format(day))
    man.act()
    cat.act()
    print('--- в конце дня ---')
    print(man)
    print(cat)
    print(home)

# citizens = [
#     Man(name='Бивис'),
#     Man(name='Батхед'),
#     Man(name='Кенни'),
# ]
#
# my_sweet_home = House()
# for citizen in citizens:
#     citizen.go_to_the_house(house=my_sweet_home)
#
# for day in range(1, 366):
#     print('================ день {} =================='.format(day))
#     for citizen in citizens:
#         citizen.act()
#     print('--- в конце дня ---')
#     for citizen in citizens:
#         print(citizen)
#     print(my_sweet_home)

# Создадим двух людей, живущих в одном доме - Бивиса и Батхеда
# Нужен класс Дом, в нем должн быть холодильник с едой и тумбочка с деньгами
# Еда пусть хранится в холодильнике в доме, а деньги - в тумбочке.

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
