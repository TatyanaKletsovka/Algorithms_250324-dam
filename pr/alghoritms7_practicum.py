import math


class DynamicArray:
    def __init__(self, capacity=10):
        self.size = 0  # Количество элементов
        self.capacity = capacity  # Начальная емкость
        self.array = [None] * self.capacity  # Инициализация массива фиксированного размера

    def append(self, data):
        # Добавление элемента в конец массива
        if self.size == self.capacity:
            self.__grow_size()  # Увеличение размера при необходимости
        self.array[self.size] = data
        self.size += 1

    def remove(self):
        # Удаление последнего элемента
        if self.size == 0:
            raise IndexError("Cannot remove from empty array")
        self.array[self.size - 1] = None
        self.size -= 1

    def remove_at(self, index):
        # Удаление элемента по индексу
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        for i in range(index, self.size - 1):
            self.array[i] = self.array[i + 1]
        self.array[self.size - 1] = None
        self.size -= 1

    import math
    def __grow_size(self):
        # Увеличение размера массива
        new_capacity = math.ceil(self.capacity * 1.125 ) # Удвоение емкости
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def insert_at(self, index, data):
        # Вставка элемента по индексу
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        if self.size == self.capacity:
            self.__grow_size()
        for i in range(self.size, index, -1):
            self.array[i] = self.array[i - 1]
        self.array[index] = data
        self.size += 1

    def clean(self):
        # Очистка всех элементов
        self.array = [None] * self.capacity
        self.size = 0

    def contains(self, data):
        # Проверка существования элемента
        for i in range(self.size):
            if self.array[i] == data:
                return True
        return False

    def is_empty(self):
        # Проверка на пустоту
        return self.size == 0

    def __str__(self):
        # Для удобного вывода элементов
        return str([self.array[i] for i in range(self.size)])


dynamic_array = DynamicArray()
dynamic_array.append(5)
dynamic_array.append(10)
dynamic_array.append(15)
print("Array after appending:", dynamic_array)  # [5, 10, 15]

dynamic_array.remove()
print("Array after removing last element:", dynamic_array)  # [5, 10]

dynamic_array.insert_at(1, 20)
print("Array after inserting at index 1:", dynamic_array)  # [5, 20, 10]

print("Array contains 20:", dynamic_array.contains(20))  # True
print("Array is empty:", dynamic_array.is_empty())  # False

dynamic_array.clean()
print("Array after cleaning:", dynamic_array)  # []


