# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПОТОЧНОМ стиле
#
# Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.
#
import os
import csv
from threading import Thread

data = "trades"


class MamkinInvestor(Thread):

    def __init__(self, file_name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._file_name = file_name
        self.result = []

    def run(self):
        tmp = []
        with open(self._file_name, 'r', encoding='utf8', newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                tmp.append(float(row['PRICE']))
            _min_price, _max_price = min(tmp), max(tmp)
            _average_price = (_min_price + _max_price) / 2
            _volatility = ((_max_price - _min_price) / _average_price) * 100
            self.result.append([row['SECID'], _min_price, _max_price, _average_price, _volatility])
            tmp.clear()


thread_list = []
result = []
max_volatility = []
zero_volatility = []
min_volatility = []


def calc_volatility(path):
    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames:
            file_path = os.path.join(dirpath, file)
            thread_list.append(MamkinInvestor(file_path))

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()

    for thread in thread_list:
        result.extend(thread.result)

    result.sort(key=lambda x: x[4], reverse=True)
    for _ in range(3):
        max_volatility.append(result.pop(0))
    result.sort(key=lambda x: x[4])
    i = 0
    for ticker in result:
        vol = ticker[4]
        if vol == 0.0:
            zero_volatility.append(ticker)
            i += 1
    del result[0:i]
    for _ in range(3):
        min_volatility.append(result.pop(0))
    print(f"max_volatility = {max_volatility}")
    print(f"zero_volatility = {zero_volatility}")
    print(f"min_volatility = {min_volatility}")


calc_volatility(data)
# for dirpath, dirnames, filenames in os.walk(self._work_folder):
#     for file in filenames:
#         file_path = os.path.join(dirpath, file)


# self._result.sort(key=lambda x: x[4], reverse=True)
#         for _ in range(3):
#             self._max_volatility.append(self._result.pop(0))
#         self._result.sort(key=lambda x: x[4])
#         i = 0
#         for ticker in self._result:
#             vol = ticker[4]
#             if vol == 0.0:
#                 self._zero_volatility.append(ticker)
#                 i += 1
#         del self._result[0:i]
#         for _ in range(3):
#             self._min_volatility.append(self._result.pop(0))
#         print(f"_max_volatility = {self._max_volatility}")
#         print(f"_zero_volatility = {self._zero_volatility}")
#         print(f"_min_volatility = {self._min_volatility}")
