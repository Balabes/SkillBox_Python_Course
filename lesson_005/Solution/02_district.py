# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

from district.soviet_street.house1.room1 import folks as sovok_h1_r1
from district.soviet_street.house1.room2 import folks as sovok_h1_r2
from district.soviet_street.house2.room1 import folks as sovok_h2_r1
from district.soviet_street.house2.room2 import folks as sovok_h2_r2

from district.central_street.house1.room1 import folks as centr_h1_r1
from district.central_street.house1.room2 import folks as centr_h1_r2
from district.central_street.house2.room1 import folks as centr_h2_r1
from district.central_street.house2.room2 import folks as centr_h2_r2

population_census = "На районе живет следующий биомусор: "

peoples_of_district = [sovok_h1_r1, sovok_h1_r2, sovok_h2_r1, sovok_h2_r2, centr_h1_r1, centr_h1_r2, centr_h2_r2,
                       centr_h2_r1]

for room in peoples_of_district:
    population_census += ','.join(room) + ","

print(population_census)
