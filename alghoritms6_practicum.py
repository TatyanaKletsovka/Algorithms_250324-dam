def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]  # Опорный элемент — средний элемент массива
        left = [x for x in arr if x < pivot]  # Все элементы меньше опорного
        middle = [x for x in arr if x == pivot]  # Элементы, равные опорному
        right = [x for x in arr if x > pivot]  # Все элементы больше опорного
        return quicksort(left) + middle + quicksort(right)

# Пример использования
arr = [3, 6, 2, 8, 10, 1, 2, 11, 1]
print(quicksort(arr))


# --------------------------------------

def iterative_quicksort(arr):
    # Стек для хранения начальных и конечных индексов подмассивов
    stack = [(0, len(arr) - 1)]

    # Выполняем сортировку, пока стек не пуст
    while stack:
        start, end = stack.pop()

        if start >= end:
            continue

        # Выбираем опорный элемент
        pivot = arr[end]
        i = start - 1

        # Разделение массива относительно опорного элемента
        for j in range(start, end):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        # Размещаем опорный элемент на его правильное место
        i += 1
        arr[i], arr[end] = arr[end], arr[i]

        # Добавляем в стек левую и правую части массива для дальнейшей сортировки
        stack.append((start, i - 1))  # Левая часть
        stack.append((i + 1, end))  # Правая часть

    return arr


# Пример использования
arr = [3, 6, 8, 10, 1, 2, 1]
print(iterative_quicksort(arr))  # Вывод: [1, 1, 2, 3, 6, 8, 10]


# -------------------------------------------

def quicksort(arr, start, end):
    if start >= end:
        return

    # Выбор последнего элемента как опорного
    pivot_index = partition(arr, start, end)

    # Рекурсивно сортируем левую и правую части
    quicksort(arr, start, pivot_index - 1)
    quicksort(arr, pivot_index + 1, end)


def partition(arr, start, end):
    # Опорный элемент — последний в подмассиве
    pivot = arr[end]
    i = start - 1  # Индекс для меньших элементов

    # Перемещаем элементы, меньшие опорного, в левую часть
    for j in range(start, end):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Меняем местами элементы

    # Размещаем опорный элемент на его окончательную позицию
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1  # Возвращаем индекс опорного элемента


# Пример использования
arr = [3, 6, 8, 10, 1, 2, 1]
quicksort(arr, 0, len(arr) - 1)
print(arr)  # Вывод: [1, 1, 2, 3, 6, 8, 10]

# ---------------------------------

def find_value(data, target_key):
    # Проходим по каждому ключу-значению в словаре
    for key, value in data.items():
        # Если ключ соответствует целевому, возвращаем значение
        if key == target_key:
            return value
        # Если значение является словарем, вызываем функцию рекурсивно
        elif isinstance(value, dict):
            result = find_value(value, target_key)
            if result is not None:
                return result
    # Возвращаем None, если ключ не найден
    return None

# Пример использования
data = {
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

# Ищем значение по ключу 'zip'
key_to_find = 'zip'
result = find_value(data, key_to_find)
print(f"Значение для ключа '{key_to_find}': {result}")
