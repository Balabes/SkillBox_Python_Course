# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.
input_file = "registrations.txt"
out_file_good = "registrations_good.log"
out_file_bad = "registrations_bad.log"


class NotNameError(Exception):
    def __str__(self):
        return type(self).__name__


class NotEmailError(Exception):
    def __str__(self):
        return type(self).__name__


def check(_line):
    name, mail, age = _line.split(" ")
    if not str.isalpha(name):
        raise NotNameError
    elif '@' not in mail and '.' not in mail:
        raise NotEmailError
    elif not (10 <= int(age) <= 99):
        raise ValueError("Age is incorrect")
    else:
        return True


with open(input_file, 'r', encoding='utf8') as src_file:
    with open(out_file_good, 'w', encoding='utf8') as good_file:
        with open(out_file_bad, 'w', encoding='utf8') as bad_file:
            for line in src_file:
                try:
                    check(line)
                    good_file.write(line)
                except (ValueError, NotEmailError, NotNameError) as ex:
                    bad_file.write(str(ex) + " " + line)
