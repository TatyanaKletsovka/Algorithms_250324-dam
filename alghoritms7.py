# def find_index(number, coll):
#     number = number - 1
#     coll.append(4)
#     return number, coll
#
# a = 7
# numbers = [1, 2, 3]
# print(find_index(a, numbers))
# print(a)
# print(numbers)
from collections import defaultdict


# Реализовать Динамический массив:
# 1. Создайте структуру DynamicArray
# 2. Реализуйте два пути создания:
    # ○ DynamicArray() - по умолчанию size = 10
    # ○ DynamicArray(capacity) - size = capacity
# 3. Реализуйте методы:
    # ○ append(data) - добавляет в конец
    # ○ remove() - удаляет последний
    # ○ removeAt(index) - удаляет по индексу
    # ○ growSize() - увеличивает размер
    # ○ insertAt(index, data) - изменяет элемент
    # ○ clean() - удаляет все элементы
    # ○ contains(data) - проверяет существует ли элемент
    # ○ isEmpty() - вернет false, если в структуре есть элемент

# import random
#
# # a = list()
# # b = [1, 2, 3]
# # c = [1, 2, 4]
#
# class DynamicArray:
#
#     def __init__(self, capacity=10):
#         self.capacity = capacity
#         self.size = 0
#         self.array = [None] * capacity
#
#     def append(self, data):
#         if self.capacity == self.size:
#             self.growSize()
#             return
#         self.array[self.size] = data
#         self.size += 1
#
#     def growSize(self):
#         pass
#
# array = DynamicArray(2)
# print(array.capacity)
# print(array.array)
# array.append(5)
# print(array.array)
# array.append(6)
# print(array.array)
# array.append(7)




def group_anagrams(data):
    result_dict = defaultdict(list)
    for word in data:
        key = ''.join(sorted(word))
        print(key)
        result_dict[key].append(word)
    return dict(result_dict)


words = ["eat", "tea", "tan", "ate", "nat", "bat"]
# функция должна вернуть список групп анаграмм:
# [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']].
res = {'aet': ['eat', 'tea', 'ate'], 'key2': ['tan', 'nat'], 'key3': ['bat']}
print(group_anagrams(words))

