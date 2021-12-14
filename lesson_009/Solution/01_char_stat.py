# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.
import zipfile
from abc import ABCMeta, abstractmethod


class TextAnalyzer(metaclass=ABCMeta):
    def __init__(self, src_file_name):
        self.statistic = {}
        self.sorted_static = []
        self.file_name = None
        self.src_file_name = src_file_name
        self.file = None
        self.alpha_counter = 0

    def get_file(self):
        if not self.src_file_name.endswith('.zip'):
            self.file_name = self.src_file_name
        else:
            zfile = zipfile.ZipFile(self.src_file_name, 'r')
            filename_in_zip = zfile.namelist()
            zfile.extract(filename_in_zip[0])
            self.file_name = filename_in_zip[0]
        # self.file = open(self.file_name, mode='r', encoding='cp1251')
        # print(self.file.readline())

    def get_alpha_static(self):
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                for char in line:
                    if char.isalpha():
                        if char in self.statistic:
                            self.statistic[char] += 1
                        else:
                            self.statistic[char] = 1
        for key, item in self.statistic.items():
            self.alpha_counter += item

    def print_static(self):
        print('+---------+----------+')
        print('|  буква  | частота  |')
        print('+---------+----------+')
        for items in self.sorted_static:
            print('|{:^9}|{:^10}|'.format(items[0], items[1]))
            # print(items)
        print('+---------+----------+')
        print('|  Итого  |{:^10}|'.format(self.alpha_counter))
        print('+---------+----------+')

    @abstractmethod
    def sort_result(self):
        pass

    def do_analyze(self):
        self.get_file()
        self.get_alpha_static()
        self.sort_result()
        self.print_static()


class TAFreqSortUp(TextAnalyzer):
    def sort_result(self):
        self.sorted_static.clear()
        self.sorted_static = sorted(self.statistic.items(), key=lambda x: x[1])
        # https: // tproger.ru / translations / python - sorting /


class TAFreqSortDown(TextAnalyzer):
    def sort_result(self):
        self.sorted_static.clear()
        self.sorted_static = sorted(self.statistic.items(), key=lambda x: x[1], reverse=True)

    class TAInAlphabetOrderSortDown(TextAnalyzer):
        def sort_result(self):
            self.sorted_static.clear()
            self.sorted_static = sorted(self.statistic.items())

    class TAInAlphabetOrderSortUp(TextAnalyzer):
        def sort_result(self):
            self.sorted_static.clear()
            self.sorted_static = sorted(self.statistic.items(), reverse=True)

    file_path = "voyna-i-mir.txt"
    ta = TAFreqSortUp(file_path)
    ta.do_analyze()
    # После выполнения первого этапа нужно сделать упорядочивание статистики
    #  - по частоте по возрастанию
    #  - по алфавиту по возрастанию
    #  - по алфавиту по убыванию
    # Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
