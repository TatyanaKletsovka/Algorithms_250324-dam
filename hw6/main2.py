def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        return quick_sort_helper(arr, 0, len(arr) - 1)

def quick_sort_helper(arr, low, high):
    if low < high:
        partition_index = partition(arr, low, high)  # основная функция выбирает опорный элемент и перемещает элементы
        quick_sort_helper(arr, low, partition_index - 1)
        quick_sort_helper(arr, partition_index + 1, high)
    return arr

def partition(arr, low, high):
    # Выбираем опорный элемент в середине диапазона
    mid = (low + high) // 2
    pivot = arr[mid]

    # Перемещаем опорный элемент в конец
    arr[mid], arr[high] = arr[high], arr[mid]

    i = low - 1
    # находим все элементы меньше опорного и перемещаем их  в начало массива
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Помещаем опорный элемент на правильную позицию / все что справа будет больше опорного элемента
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# Проверяем работу сортировки, генерируем случайный массив данных и сортируем его
import random
def generate_random_array(length, min_value=0, max_value=100):
    return [random.randint(min_value, max_value) for _ in range(length)]

array_length = 21
test_array = generate_random_array(array_length, 1, 100)

print("Исходный массив:", test_array)
sorted_array = quick_sort(test_array)
print("Отсортированный массив:", sorted_array)


# -------------


def partition(arr, low, high):
    # Выбираем опорный элемент в середине диапазона
    mid = (low + high) // 2
    pivot = arr[mid]

    # Перемещаем опорный элемент в конец
    arr[mid], arr[high] = arr[high], arr[mid]

    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort_iterative(arr):
    size = len(arr)
    stack = [(0, size - 1)]

    while stack:
        low, high = stack.pop()

        if low < high:
            pivot_index = partition(arr, low, high)

            # Если есть элементы слева от опорного, добавляем их в стек
            if pivot_index - 1 > low:
                stack.append((low, pivot_index - 1))

            # Если есть элементы справа от опорного, добавляем их в стек
            if pivot_index + 1 < high:
                stack.append((pivot_index + 1, high))

    return arr


 # Проверяем работу сортировки, генерируем случайный массив данных и сортируем его
import random
def generate_random_array(length, min_value=0, max_value=100):
    return [random.randint(min_value, max_value) for _ in range(length)]

array_length = 21
test_array = generate_random_array(array_length, 1, 100)

print("Исходный массив:", test_array)
sorted_array = quick_sort(test_array)
print("Отсортированный массив:", sorted_array)