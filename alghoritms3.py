# n = [1, 2, 3, 4, 5, 6, 7]
# result = 0
#
# for i in n:
#     result += i
#
# print(result)

# n = 5
# while n >= 0:
#     print(n)
#     n -= 1
#
# n = [1, 2, 3, 4, 5, 6, 7]
# result = 0
#
# for i in n:
#     print(i)


# n = 3
# if n == 1:  # базовый случай
#     return 1
# else:
#     return n + recursive_sum(n - 1)  # рекурсивный вызов


# n = [1, 2, 3, 4, 5, 6, 7]
# n.append(8)
# n.append(9)
# print(n.pop())
# print(n)


# def recursive_sum(n):
#     s = ''
#     if n == 1:  # базовый случай
#         return 1
#     else:
#         return n + recursive_sum(n - 1)  # рекурсивный вызов
#
# print(recursive_sum(3))  # Вывод: 15 (1 + 2 + 3 + 4 + 5)

# def func_recursive(n):
#     if n==0:
#         return 0
#     res = (n-1)+func_recursive(n-1)
#     print ("res=", res, "; n=", n)
#     return res
# print(func_recursive(5))

# def func_recursive(x, y):
#     if x==0:
#         return y
#     else:
#         res = func_recursive(x-1, x+y)
#         print("res=", res, "; x=", x, "; y=", y)
#         return res
#
# func_recursive(5, 10)
# print()

# def func_iterative(x, y):
#     xs = []
#     ys = []
#     res = 0
#     for i in range(x):
#         res = x + res
#         xs.append(i + 1)
#         ys.append(y)
#         y = (x-i)+y
#     for x, y in zip(xs, ys[::-1]):
#         print("res=", res, "; x=", x, "; y=", y)
#
#     return y
# func_iterative(5, 10)
#

# def func_iterative2(x, y):
#     arr = []
#     while x != 0:
#         arr.append((x, y))
#         y = x + y
#         x = x - 1
#     print(arr)
#
#     for x, y in arr[::-1]:
#         print("x =", x, "; y =", y)
#
#     return y
#
#
# result_it = func_iterative2(5, 10)
# print(result_it)


original_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(id(original_list))
new_list = original_list[:]
print(id(new_list))
original_list.append("Hello")
original_list[0].append("Hi")
print(original_list)
print(new_list)


# Алгоритм глубокого копирования списка с вложенными списками
def deep_copy(lst):
    # Создаем новый список, в который будем копировать элементы
    new_lst = []

    for item in lst:
        # Если элемент является списком, копируем его рекурсивно
        if isinstance(item, list):
            new_lst.append(deep_copy(item))
        else:
            # Если элемент не является списком, просто добавляем его
            new_lst.append(item)

    return new_lst

# Оригинальный список с вложенными списками
original_list = [[1, 2, 3], "Hi", [4, 5, 6], [7, 8, 9]]

# Глубокая копия списка с использованием нашей функции
deep_copied_list = deep_copy(original_list)

# Изменим элемент в оригинальном списке
original_list[0][0] = 99

# Выводим результаты
print("Оригинальный список:", original_list)  # [[99, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Глубокая копия:", deep_copied_list)    # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
