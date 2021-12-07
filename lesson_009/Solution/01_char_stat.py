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
from pprint import pprint


class TextAnalyzer:
    def __init__(self, src_file_name):
        self.statistic = {}
        self.file_name = None
        self.src_file_name = src_file_name
        self.file = None
        self.alpha_counter = 0

    def get_file(self):
        if self.src_file_name.endswith('.zip'):
            zfile = zipfile.ZipFile(self.src_file_name, 'r')
            for filename in zfile.namelist():
                zfile.extract(filename)
            self.file_name = filename
        else:
            self.file_name = self.src_file_name
        # self.file = open(self.file_name, mode='r', encoding='cp1251')
        # print(self.file.readline())

    def calculate_static(self):
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
        pprint(self.statistic)
        print(f"Итого букв = {self.alpha_counter}")



file_path = "voyna-i-mir.txt"
ta = TextAnalyzer(file_path)
ta.get_file()
ta.calculate_static()
# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
