# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

from abc import ABCMeta, abstractmethod

eventstxt = "events.txt"
outtxt = "out.txt"


class LogParser(metaclass=ABCMeta):
    @abstractmethod
    def group(self):
        pass

    def __init__(self, src_file_name, result_file_name):
        self._src_file = src_file_name
        self._result_file = result_file_name
        self._result = {}
        self.group_by_minutes = 17
        self.group_by_hours = 14
        self.group_by_days = 11
        self.group_by_month = 8
        self.group_by_years = 5
        self._group_by = None
        self.group()

    def get_stat(self):
        with open(self._src_file, 'r', encoding='utf8') as file:
            for line in file:
                date = line[:self._group_by] + "]"
                if "NOK" in line:
                    if date in self._result.keys():
                        self._result[date] += 1
                    else:
                        self._result[date] = 1

    def print_result(self):
        with open(self._result_file, 'w', encoding='utf8') as file:
            for items in self._result.items():
                file.write(f"{items[0]} {items[1]}\r")
                print(items)


class LogParserGroupByMinutes(LogParser):
    def group(self):
        self._group_by = self.group_by_minutes


class LogParserGroupByHours(LogParser):
    def group(self):
        self._group_by = self.group_by_hours


class LogParserGroupByDays(LogParser):
    def group(self):
        self._group_by = self.group_by_days


class LogParserGroupByMonths(LogParser):
    def group(self):
        self._group_by = self.group_by_month


class LogParserGroupByYears(LogParser):
    def group(self):
        self._group_by = self.group_by_years


# lp = LogParserGroupByMinutes(eventstxt, outtxt)
lp = LogParserGroupByHours(eventstxt, outtxt)
# lp = LogParserGroupByMonths(eventstxt, outtxt)
# lp = LogParserGroupByDays(eventstxt, outtxt)
# lp = LogParserGroupByYears(eventstxt, outtxt)

lp.get_stat()
lp.print_result()
# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
