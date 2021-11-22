# -*- coding: utf-8 -*-

# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...
from room_1 import folks as r1_folks
from room_2 import folks as r2_folks

result_string = "В комнате room_1 живут:"

for person in r1_folks:
    result_string = result_string + " " + person
print(result_string)

result_string = "В комнате room_2 живёт:"
for person in r2_folks:
    result_string = result_string + " " + person
print(result_string)
