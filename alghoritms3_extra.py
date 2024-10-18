# def func(n):
#     if n <= 1: # base case
#         return 1
#     return n * func(n-1)
# # 1
# # 2 * func(n-1) -> 2 * 1 = 2
# # 3 * func(n-1) -> 3 * 2 = 6
# # 4 * func(n-1) -> 4 * 6 = 24
# # 5 * func(n-1) -> 5 * 24 = 120
# print(func(5))  # -> 120


# def func2(n):
#     if n >= 100: # base case
#         return 1
#     else:
#         print(n)
#         return n * func2(n-1)
#
# print(func2(5))

# n = 5
# while n != 100:
#     print(n)
#     n -= 1


# def recursive_sum(n):
#     if n == 1:  # базовый случай
#         return 1
#     else:
#         return n + recursive_sum(n - 1)  # рекурсивный вызов
#
# print(recursive_sum(3))  # Вывод: 15 (1 + 2 + 3 + 4 + 5)


# # Нахождение факториала числа n! с помощью рекурсии.
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
# print(factorial(5))  # Вывод: 120 (5 * 4 * 3 * 2 * 1)


# # Нахождение суммы всех цифр числа с использованием рекурсии.
# def sum_of_digits(n):
#     if n == 0:
#         return 0
#     else:
#         return n % 10 + sum_of_digits(n // 10)
#
# print(sum_of_digits(1234))  # Вывод: 10 (1 + 2 + 3 + 4)


# # Алгоритм глубокого копирования списка с вложенными списками
# def deep_copy(lst):
#     # Создаем новый список, в который будем копировать элементы
#     new_lst = []
#
#     for item in lst:
#         # Если элемент является списком, копируем его рекурсивно
#         if isinstance(item, list):
#             new_lst.append(deep_copy(item))
#         else:
#             # Если элемент не является списком, просто добавляем его
#             new_lst.append(item)
#
#     return new_lst
#
# # Оригинальный список с вложенными списками
# original_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# # Глубокая копия списка с использованием нашей функции
# deep_copied_list = deep_copy(original_list)
#
# # Изменим элемент в оригинальном списке
# original_list[0][0] = 99
#
# # Выводим результаты
# print("Оригинальный список:", original_list)  # [[99, 2, 3], [4, 5, 6], [7, 8, 9]]
# print("Глубокая копия:", deep_copied_list)    # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


# # Проверка четности и нечетности
# def is_even(n):
#     if n == 0:
#         return True
#     return is_odd(n - 1)
#
# def is_odd(n):
#     if n == 0:
#         return False
#     return is_even(n - 1)
#
# # Проверка
# print(is_even(4))  # True
# print(is_odd(7))   # True
