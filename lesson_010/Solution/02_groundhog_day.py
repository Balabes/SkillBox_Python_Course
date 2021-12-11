# -*- coding: utf-8 -*-

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.
import random
import time

ENLIGHTENMENT_CARMA_LEVEL = 777


class IamGodError(Exception):
    def __str__(self):
        return type(self).__name__


class DrunkError(Exception):
    def __str__(self):
        return type(self).__name__


class CarCrashError(Exception):
    def __str__(self):
        return type(self).__name__


class GluttonyError(Exception):
    def __str__(self):
        return type(self).__name__


class DepressionError(Exception):
    def __str__(self):
        return type(self).__name__


class SuicideError(Exception):
    def __str__(self):
        return type(self).__name__


def one_day():
    dice = random.randint(1, 13)
    if dice == 13:
        dice = random.randint(1, 6)
        if dice == 1:
            raise IamGodError
        elif dice == 2:
            raise DrunkError
        elif dice == 3:
            raise CarCrashError
        elif dice == 4:
            raise GluttonyError
        elif dice == 5:
            raise DepressionError
        else:
            raise SuicideError
    else:
        return random.randint(1, 7)


karma = 0
while karma < ENLIGHTENMENT_CARMA_LEVEL:
    try:
        karma += one_day()
    except Exception as ex:
        with open("log.txt", 'a', encoding='utf8') as file:
            file.write(f"{time.ctime()}, Error = {ex}\r")

print("Groundhog Day is OVER!")
# https://goo.gl/JnsDqu
