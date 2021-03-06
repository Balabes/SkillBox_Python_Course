# -*- coding: utf-8 -*-

# Игра «Быки и коровы»
# https://goo.gl/Go2mb9
#
# Правила:
# Компьютер загадывает четырехзначное число, все цифры которого различны
# (первая цифра числа отлична от нуля). Игроку необходимо разгадать задуманное число.
# Игрок вводит четырехзначное число c неповторяющимися цифрами,
# компьютер сообщают о количестве «быков» и «коров» в названном числе
# «бык» — цифра есть в записи задуманного числа и стоит в той же позиции,
#       что и в задуманном числе
# «корова» — цифра есть в записи задуманного числа, но не стоит в той же позиции,
#       что и в задуманном числе
#
# Например, если задумано число 3275 и названо число 1234,
# получаем в названном числе одного «быка» и одну «корову».
# Очевидно, что число отгадано в том случае, если имеем 4 «быка».
#
# Формат ответа компьютера
# > быки - 1, коровы - 1


# Составить отдельный модуль mastermind_engine, реализующий функциональность игры.
# В этом модуле нужно реализовать функции:
#   загадать_число()
#   проверить_число(NN) - возвращает словарь {'bulls': N, 'cows': N}
# Загаданное число хранить в глобальной переменной.
# Обратите внимание, что строки - это список символов.
#
# В текущем модуле (lesson_006/01_mastermind.py) реализовать логику работы с пользователем:
#   модуль движка загадывает число
#   в цикле, пока число не отгадано
#       у пользователя запрашивается вариант числа
#       модуль движка проверяет число и выдает быков/коров
#       результат быков/коров выводится на консоль
#  когда игрок угадал таки число - показать количество ходов и вопрос "Хотите еще партию?"
#
# При написании кода учитывайте, что движок игры никак не должен взаимодействовать с пользователем.
# Все общение с пользователем делать в текущем модуле. Представьте, что движок игры могут использовать
# разные клиенты - веб, чатбот, приложение, етс - они знают как спрашивать и отвечать пользователю.
# Движок игры реализует только саму функциональность игры.
# Это пример применения SOLID принципа (см https://goo.gl/GFMoaI) в архитектуре программ.
# Точнее, в этом случае важен принцип единственной ответственности - https://goo.gl/rYb3hT

import mastermind_engine as engine

print(
    "Правила:\r\n"
    "Компьютер загадывает четырехзначное число, все цифры которого различны (первая цифра числа отлична\r\n"
    "от нуля). Игроку необходимо разгадать задуманное число. Игрок вводитчетырехзначное число c \r\n"
    "неповторяющимися цифрами,компьютер сообщают о количестве «быков» и «коров» названном числе «бык» — цифра \r\n"
    "есть в записи задуманного числа и стоит в той же позиции, что и в задуманном числе «корова» — цифра есть в\r\n"
    "записи задуманного числа, но не стоит в той же позиции, что и в задуманном числе")

state = True
while state:
    engine.hidden_number = engine.hidden_number_init()
    print(engine.hidden_number)
    engine.try_cnt = 0
    while True:
        num = str(input('Введите 4-х значное число:'))
        engine.try_cnt += 1
        if len(num) != 4:
            print("Ты дурак? Сказано же: 4 ЦИФРЫ!")
            break
        res = engine.check_input(num)
        print(f"Быки - {res['bull']}, Коровы - {res['cow']}")
        if res['bull'] == 4:
            print("Поздравляю! ты победил. Доволен? Чувствуешь себя умнее машины, чухан ебаный..?")
            print(f"Ты потратил {engine.try_cnt} попыток")
            ans = input("Ещё раз? y/n")
            if ans == 'n' or ans == 'N':
                state = False
                break
            else:
                break

