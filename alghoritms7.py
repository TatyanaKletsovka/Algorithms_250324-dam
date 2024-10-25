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

import random

# a = list()
# b = [1, 2, 3]
# c = [1, 2, 4]

class DynamicArray:

    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.array = [None] * capacity

    def append(self, data):
        if self.capacity == self.size:
            self.growSize()
            return
        self.array[self.size] = data
        self.size += 1

    def growSize(self):
        pass

array = DynamicArray(2)
print(array.capacity)
print(array.array)
array.append(5)
print(array.array)
array.append(6)
print(array.array)
array.append(7)

