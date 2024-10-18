# def hanoi(n, source, target, auxiliary):
#     if n == 1:
#         print(f"Переместить диск 1 с {source} на {target}")
#         return
#     # Переместить n-1 диск с source на auxiliary
#     hanoi(n - 1, source, auxiliary, target)
#     # Переместить n-й диск с source на target
#     print(f"Переместить диск {n} с {source} на {target}")
#     # Переместить n-1 диск с auxiliary на target
#     hanoi(n - 1, auxiliary, target, source)
#
# # Пример использования
# n = 3  # Количество дисков
# hanoi(n, 'A', 'C', 'B')






# 1 интерация
# def fib_iterative(n):
#     a, b = 0, 1
#     for _ in range(n - 1):
#         a, b = b, a + b
#     return a

# def fib_iterative(n):
#     a, b = 0, 1
#     print(a, b, sep=' ', end=' ')
#     for _ in range(n - 2):
#         a, b = b, a + b
#         print(b, end=' ')
#     print()
#     return b
#
# print(fib_iterative(7))

# 0 1 1 2 3 5 8 13



# 1 рекурсия
# def fib_recursive(n):
#     print(f'n: {n}:')
#     if n == 1:
#         return 0
#     if n == 2:
#         return 1
#     n1 = fib_recursive(n-1)
#     n2 = fib_recursive(n-2)
#     print(f'n: {n}, n1: {n1}, n2: {n2}')
#     return n1 + n2
#
# print(fib_recursive(7))

# 0 1 1 2 3 5 8 13 21 34 55
# 1 2 3 4 5 6 7 8  9  10 11

# def fib_recursive(n):
#     if n == 1:
#         return 0
#     if n == 2:
#         return 1
#     return fib_recursive(n-1) + fib_recursive(n-2)
#
# print(fib_recursive(10))

# def recursive_sum(n):
#     if n == 1:  # базовый случай
#         return 1
#     else:
#         return n + recursive_sum(n - 1)  # рекурсивный вызов
#
# print(recursive_sum(5))  # Вывод: 15 (1 + 2 + 3 + 4 + 5)

def recursive_sum(n):
    if n != 0:  # базовый случай
        print(n)
        recursive_sum(n - 1)

print(recursive_sum(5))  # Вывод: 15 (1 + 2 + 3 + 4 + 5)
print(recursive_sum(0))  # Вывод: 15 (1 + 2 + 3 + 4 + 5)