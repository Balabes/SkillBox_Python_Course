# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000
total_expenses = 0
total_grants = educational_grant * 10

month_cnt = 0
while month_cnt < 10:
    if month_cnt == 0:
        total_expenses += expenses
    else:
        expenses *= 1.03
        total_expenses += expenses
    month_cnt += 1
print(f"Студенту надо попросить {round(total_expenses - total_grants, 2)} рублей")
