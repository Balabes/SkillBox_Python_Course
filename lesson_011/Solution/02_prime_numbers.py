# -*- coding: utf-8 -*-


# Есть функция генерации списка простых чисел


# def get_prime_numbers(n):
#     prime_numbers = []
#     for number in range(2, n + 1):
#         for prime in prime_numbers:
#             if number % prime == 0:
#                 break
#         else:
#             prime_numbers.append(number)
#     return prime_numbers
#
#
# print(get_prime_numbers(100))


# Часть 1
# На основе алгоритма get_prime_numbers создать класс итерируемых обьектов,
# который выдает последовательность простых чисел до n
#
# Распечатать все простые числа до 10000 в столбик


# class PrimeNumbers:
#     def __init__(self, n):
#         self._n = n
#         self._prime_numbers = [2]
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         for nmbr in range(self._prime_numbers[-1], self._n + 1):
#             for prime in self._prime_numbers:
#                 if nmbr == self._n:
#                     raise StopIteration()
#                 if nmbr % prime == 0:
#                     break
#             else:
#                 self._prime_numbers.append(nmbr)
#                 return nmbr
#
#
# prime_number_iterator = PrimeNumbers(n=100)
# for number in prime_number_iterator:
#     print(number)

# Часть 2
# Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# Распечатать все простые числа до 10000 в столбик


def prime_numbers_generator(n):
    prime_numbers = []
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
            yield number


#
#
# for number in prime_numbers_generator(n=10000):
#     print(number)


# Часть 3
# Написать несколько функций-фильтров, которые выдает True, если число:
# 1) "счастливое" в обыденном пониманиии - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+2 == 8+3 -> True
# 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например 723327 и 101
# 3) придумать свою (https://clck.ru/GB5Fc в помощь)
#
# Подумать, как можно применить функции-фильтры к полученной последовательности простых чисел
# для получения, к примеру: простых счастливых чисел, простых палиндромных чисел,
# простых счастливых палиндромных чисел и так далее. Придумать не менее 2х способов.
#
# Подсказка: возможно, нужно будет добавить параметр в итератор/генератор.
# from itertools import count


def happy_filter(number):
    src_str = str(number)
    src_str_len = len(src_str)
    left_sum = right_sum = 0
    left_str = right_str = ""
    if src_str_len % 2 == 0:  # чет
        left_str = src_str[:src_str_len // 2]
        right_str = src_str[src_str_len // 2:]
    else:
        left_str = src_str[:src_str_len // 2]
        right_str = src_str[src_str_len // 2 + 1:]
    for ch in left_str:
        left_sum += int(ch)
    for ch in right_str:
        right_sum += int(ch)
    if left_sum == right_sum:
        return True
    else:
        return False


# print(happy_filter(1234321))


def pereverten_filter(number):
    src_str = str(number)
    reversed_str = src_str[::-1]
    if src_str == reversed_str:
        return True
    else:
        return False


# print(pereverten_filter(123456789))

for num in filter(pereverten_filter, prime_numbers_generator(n=100000)):
    print(num, end=" ")
