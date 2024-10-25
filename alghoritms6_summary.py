# fixed to readable
def partition(array, low, high):
    # Опорный элемент — последний в подмассиве
    pivot = array[high]
    i = low  # Индекс куда вставлять меньшие элементы

    # Перемещаем элементы, меньшие опорного, в левую часть
    for j in range(low, high):
        if array[j] <= pivot:
            array[i], array[j] = array[j], array[i]  # Меняем местами элементы
            i += 1

    # Размещаем опорный элемент на его окончательную позицию
    array[i], array[high] = array[high], array[i]
    return i  # Возвращаем индекс опорного элемента

def quicksort(array, low, high):
    if low >= high:
        return

    # Выбор последнего элемента как опорного
    pivot_index = partition(array, low, high)

    # Рекурсивно сортируем левую и правую части
    quicksort(array, low, pivot_index - 1)
    quicksort(array, pivot_index + 1, high)

# Пример использования
arr = [3, 6, 8, 1, 10, 1, 2, 4]
quicksort(arr, 0, len(arr) - 1)
print(arr)  # Вывод: [1, 1, 2, 3, 6, 8, 10]

#
#
# # -------------------------------
#


def partition(array, low, high):
    # Опорный элемент — последний в подмассиве
    pivot = array[high]
    i = low - 1  # Индекс куда вставлять меньшие элементы

    # Перемещаем элементы, меньшие опорного, в левую часть
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]  # Меняем местами элементы

    # Размещаем опорный элемент на его окончательную позицию
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1  # Возвращаем индекс опорного элемента

def quicksort(array, low, high):
    if low >= high:
        return

    # Выбор последнего элемента как опорного
    pivot_index = partition(array, low, high)

    # Рекурсивно сортируем левую и правую части
    quicksort(array, low, pivot_index - 1)
    quicksort(array, pivot_index + 1, high)

# Пример использования
arr = [3, 6, 8, 10, 1, 2, 4]
quicksort(arr, 0, len(arr) - 1)
print(arr)  # Вывод: [1, 1, 2, 3, 6, 8, 10]

#
#
#
#
# # -----------------------------------------------------------------------------------
#
#
#
#
# def iterative_quicksort(arr):
#     # Стек для хранения начальных и конечных индексов подмассивов
#     stack = [(0, len(arr) - 1)]
#
#     # Выполняем сортировку, пока стек не пуст
#     while stack:
#         start, end = stack.pop()
#
#         if start >= end:
#             continue
#
#         # Выбираем опорный элемент
#         pivot = arr[end]
#         i = start - 1
#
#         # Разделение массива относительно опорного элемента
#         for j in range(start, end):
#             if arr[j] < pivot:
#                 i += 1
#                 arr[i], arr[j] = arr[j], arr[i]
#
#         # Размещаем опорный элемент на его правильное место
#         i += 1
#         arr[i], arr[end] = arr[end], arr[i]
#
#         # Добавляем в стек левую и правую части массива для дальнейшей сортировки
#         stack.append((start, i - 1))  # Левая часть
#         stack.append((i + 1, end))  # Правая часть
#
#     return arr
#
#
# # Пример использования
# arr = [3, 6, 8, 10, 1, 2, 4]
# print(iterative_quicksort(arr))  # Вывод: [1, 1, 2, 3, 6, 8, 10]
#




# -----------------------------------------------------------------------------------




def find_value(data, key):
    if key in data:
        return data[key]
    for el in data.values():
        if isinstance(el, dict):
            return find_value(el, key)


data_with_addresses = {
    'name': 'Alice',
    'info': {
        'age': 30,
        'address': {
            'city': 'New York',
            'zip': '10001'
        }
    },
    'job': {
        'position': 'Developer',
        'company': {
            'name': 'Tech Corp',
            'location': {
                'city': 'San Francisco',
                'zip': '94105'
            }
        }
    }
}
print(find_value(data_with_addresses, 'cidfgdfgty'))
