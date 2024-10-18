# def find_magic_index_loop(array):
#     for i in range(len(array)):
#         if array[i] == i:
#             return i
#     return -1  # Возврат -1, если магического индекса нет
#
# # Пример использования
# arr = [-1, -2, 1, 3, 5, 8, 11, 14, 15, 19]
# magic_index = find_magic_index_loop(arr)
# if magic_index != -1:
#     print(f"Магический индекс: {magic_index}")
# else:
#     print("Магического индекса нет")
#
#
#
#
#
# def magic_index(array, currentIndex, maxIndex):
#     if currentIndex > maxIndex:
#         return -1  # Если дошли до конца и не нашли магический индекс
#
#     if array[currentIndex] == currentIndex:
#         return currentIndex  # Нашли магический индекс
#
#     return magic_index(array, currentIndex + 1, maxIndex)  # Проверяем следующий элемент
#
# # Пример использования
# arr = [-1, 1, 2, 4, 5, 8, 11, 14, 15, 19]
# print(magic_index(arr, 0, len(arr) - 1))
#
#
#
#
#
#
# def magic_index(array, minIndex=None, maxIndex=None):
#
#     if not minIndex:
#         minIndex = 0
#     if not maxIndex:
#         maxIndex = len(array) - 1
#
#     if minIndex > maxIndex:
#         return -1
#     midIndex = (minIndex + maxIndex) // 2
#
#     if array[midIndex] == midIndex:
#         return midIndex
#
#     if array[midIndex] < midIndex:
#         return magic_index(array, midIndex+1, maxIndex)
#     else:
#         return magic_index(array, minIndex , midIndex-1)
#
# arr=[-1, 1, 2, 4, 5, 8, 11, 14, 15, 19]
#
# print(magic_index(arr))



# ----------------------------------------------------

def get_max_element(array, minIndex, maxIndex):
    while minIndex <= maxIndex:
        midIndex = (minIndex + maxIndex) // 2

        # Проверяем, является ли текущий элемент максимальным
        if (midIndex == 0 or array[midIndex] > array[midIndex - 1]) and (
                midIndex == len(array) - 1 or array[midIndex] > array[midIndex + 1]):
            return array[midIndex]

        # Если средний элемент меньше левого соседа, ищем в левой части
        if array[midIndex - 1] > array[midIndex]:
            maxIndex = midIndex - 1
        # Иначе ищем в правой части
        else:
            minIndex = midIndex + 1

    return -1  # Если ничего не найдено (хотя по условию задачи такого не будет)


# Пример использования
arr = [-1, 1, 2, 4, 5, 8, 11, 10, 9, 8]
print(get_max_element(arr, 0, len(arr) - 1))  # Вывод: 11

# def get_max_element(array, minIndex, maxIndex):
#
#     if minIndex > maxIndex:
#         return -1
#     midIndex = (minIndex + maxIndex) // 2
#
#     if array[midIndex] > array[midIndex+1] and array[midIndex] > array[midIndex-1]:
#         return array[midIndex]
#     if array[midIndex-1] > array[midIndex] and array[midIndex]>array[midIndex+1]:
#         return get_max_element(array, minIndex, midIndex-1)
#     else:
#         return get_max_element(array, midIndex+1 , maxIndex)
#
# arr=[-1, 1, 2, 4, 5, 8, 11, 10, 9, 8]
#
# print(get_max_element(arr, 0, 9))


