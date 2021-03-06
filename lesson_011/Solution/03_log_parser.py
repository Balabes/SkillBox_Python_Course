# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234
# [2018-05-14 19:38:25.873687] NOK
from collections import OrderedDict

src_file = "events.txt"
time_pos = len("[2018-05-17 01:57")
result_pos = len("[2018-05-14 19:38:25.873687] ")


def log_parser_generator(filename):
    events = OrderedDict()
    key = None
    with open(filename, 'r', encoding='utf8') as file:
        for line in file:
            key = line[:time_pos] + "]"
            char = line[result_pos:result_pos + 1]
            if char == 'N':
                if key not in events:
                    if events.values():
                        yield next(reversed(events.items()))
                    events[key] = 1
                else:
                    events[key] += 1


grouped_events = log_parser_generator(src_file)
for group_time, event_count in grouped_events:
    print(f'[{group_time}] {event_count}')

# log_parser_generator(src_file)
