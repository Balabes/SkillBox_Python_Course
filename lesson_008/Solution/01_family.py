# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint


# Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.
class House:
    def __init__(self):
        self.money = 100
        self.food = 50
        self.dirt = 0
        self.cat_food = 30

    def make_mess(self):
        self.dirt += 5

    def __str__(self):
        return "Дом: деньги = {}, еда = {}, кошачья еда = {}, грязь = {}".format(self.money, self.food, self.cat_food,
                                                                                 self.dirt)


class Man:
    def __init__(self, name, house):
        self.name = name
        self.hungry = 30
        self.happiness = 100
        self.home = house
        self.live = True

    def __str__(self):
        return "Я - {}, сытость = {}, счастье = {}".format(self.name, self.hungry, self.happiness)

    def eat(self):
        if self.home.food > 30:
            self.hungry += 30
            self.home.food -= 30

    def caress_cat(self, cat):
        if cat:
            self.happiness += 5
            cprint('{} гладит котика {}...'.format(self.name, cat.name), color='white')


class Husband(Man):

    def __init__(self, name, house):
        super().__init__(name=name, house=house)

    def __str__(self):
        return super().__str__()

    def act(self, cat):
        if self.live:
            if self.hungry <= 0 or self.happiness <= 10:
                self.live = False
                cprint('{} умер...'.format(self.name), color='red')
                return
            dice = randint(1, 6)
            if self.hungry < 20:
                self.eat()
            elif self.happiness < 20:
                self.gaming()
            elif self.home.money < 150:
                self.work()
            elif dice == 1:
                self.work()
            elif dice == 2:
                self.eat()
            elif dice == 3:
                self.gaming()
            elif dice == 4:
                self.caress_cat(cat)
            else:
                cprint('{} бездельничает...'.format(self.name), color='green')

    def eat(self):
        super(Husband, self).eat()
        cprint('{} ест...'.format(self.name), color='green')

    def work(self):
        self.hungry -= 10
        self.home.money += 150
        cprint('{} работает...'.format(self.name), color='green')

    def gaming(self):
        self.hungry -= 10
        self.happiness += 20
        cprint('{} играет...'.format(self.name), color='green')


class Wife(Man):

    def __init__(self, name, house):
        super().__init__(name=name, house=house)
        self.fur_coat_count = 0

    def __str__(self):
        return super().__str__() + ", шубы = {}".format(self.fur_coat_count)

    def act(self, cat):
        if self.live:
            if self.hungry <= 0 or self.happiness <= 10:
                self.live = False
                cprint('{} умер...'.format(self.name), color='red')
                return
            dice = randint(1, 6)
            if self.hungry < 20:
                self.eat()
            elif self.happiness < 20:
                self.buy_fur_coat()
            elif self.home.food < 60 or self.home.cat_food < 20:
                self.shopping()
            elif self.home.dirt > 100:
                self.clean_house()
            elif dice == 1:
                self.clean_house()
            elif dice == 2:
                self.eat()
            elif dice == 3:
                self.buy_fur_coat()
            elif dice == 4:
                self.caress_cat(cat)
            else:
                cprint('{} бездельничает...'.format(self.name), color='magenta')

    def eat(self):
        super(Wife, self).eat()
        cprint('{} ест...'.format(self.name), color='magenta')

    def shopping(self):
        cprint('{} в магазине...'.format(self.name), color='magenta')
        self.hungry -= 10
        if self.home.cat_food < 20:
            if self.home.money >= 30:
                self.home.cat_food += 30
                self.home.money -= 30
            else:
                cprint("Нет денег на кошачью еду".format(self.name), color='red')
        if self.home.food < 60:
            if self.home.money >= 100:
                self.home.food += 100
                self.home.money -= 100
            else:
                cprint("Нет денег на еду".format(self.name), color='red')

    def buy_fur_coat(self):
        cprint('{} ушла за шубой...'.format(self.name), color='magenta')
        self.hungry -= 10
        if self.home.money >= 350:
            self.fur_coat_count += 1
            self.home.money -= 350
            self.happiness += 60

    def clean_house(self):
        cprint('{} убирает...'.format(self.name), color='magenta')
        self.hungry -= 10
        if self.home.dirt < 100:
            self.home.dirt = 0
        else:
            self.home.dirt -= 100


class Child(Man):

    def __init__(self, name, house):
        super().__init__(name, house)
        self.happiness = 100

    def __str__(self):
        return super().__str__()

    def act(self):
        dice = randint(1, 3)
        if self.hungry <= 20:
            self.eat()
        elif dice == 1:
            self.sleep()
        else:
            cprint('{} бездельничает...'.format(self.name), color='yellow')

    def eat(self):
        if self.home.food >= 10:
            self.hungry += 20
            self.home.food -= 10
            cprint('{} ест...'.format(self.name), color='yellow')
        else:
            cprint('{} нет еды...'.format(self.name), color='red')

    def sleep(self):
        self.hungry -= 5
        cprint('{} спит...'.format(self.name), color='yellow')


class Cat:

    def __init__(self, name, house):
        self.name = name
        self.home = house
        self.hungry = 30
        self.live = True

    def act(self):
        if self.live:
            if self.hungry <= 0:
                self.live = False
                cprint('{} умер...'.format(self.name), color='red')
                return
            dice = randint(1, 4)
            if self.hungry < 20:
                self.eat()
            elif dice == 1:
                self.soil()
            elif dice == 2:
                self.sleep()
            else:
                cprint('{} бездельничает...'.format(self.name), color='white')

    def eat(self):
        if self.home.cat_food >= 10:
            self.hungry += 20
            self.home.cat_food -= 10
        else:
            cprint('{} нечего кушац...'.format(self.name), color='white')

    def sleep(self):
        self.hungry -= 10
        cprint('{} спит...'.format(self.name), color='white')

    def soil(self):
        self.home.dirt += 5
        self.hungry -= 10
        cprint('Шерстяной пидор дерет обои...', color='white')

    def __str__(self):
        return "Я кот - {}, сытость = {}".format(self.name, self.hungry)


home = House()
serge = Husband(name='Сережа', house=home)
masha = Wife(name='Маша', house=home)
murzik = Cat(name='Мурзик', house=home)
kolya = Child(name='Коля', house=home)

for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    kolya.act()
    serge.act(murzik)
    masha.act(murzik)
    murzik.act()
    home.make_mess()
    if home.dirt > 90:
        masha.happiness -= 10
        serge.happiness -= 10
    cprint(serge.__str__(), color='green')
    cprint(masha.__str__(), color='magenta')
    cprint(kolya.__str__(), color='yellow')
    cprint(murzik.__str__(), color='white')
    cprint(home.__str__(), color='cyan')

#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов

# Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

# class Child:
#
#     def __init__(self):
#         pass
#
#     def __str__(self):
#         return super().__str__()
#
#     def act(self):
#         pass
#
#     def eat(self):
#         pass
#
#     def sleep(self):
#         pass


# Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


# home = House()
# serge = Husband(name='Сережа')
# masha = Wife(name='Маша')
# kolya = Child(name='Коля')
# murzik = Cat(name='Мурзик')
#
# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     serge.act()
#     masha.act()
#     kolya.act()
#     murzik.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(kolya, color='cyan')
#     cprint(murzik, color='cyan')

# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')
