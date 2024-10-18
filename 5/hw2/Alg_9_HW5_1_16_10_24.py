# Деление массива на 2 половины:
def merge_sort(array):
    if len(array) > 1:  # Длина массива для деления должна быть больше 1
        middle = len(array) // 2  # Cередина массива

        # Делим массив на 2 половины
        left_half = array[:middle] # Срез от начала массива до его середины
        right_half = array[middle:] # Срез от середины массива до его конца

        # Рекурсивно применяем merge_sort к обеим половинам
        merge_sort(left_half)
        merge_sort(right_half)

        # Сливаем две половины после сортировки
        merge(array, left_half, right_half)

# Слияние массивов:
def merge(array, left_half, right_half):
    left_index = right_index = array_index = 0  # Определяем индексы

    # Слияние элементов в основной массив, до тех пор, пока они есть в обоих частях массива
    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] < right_half[right_index]:  # Если элемент в левой половине меньше
            array[array_index] = left_half[left_index]  # Тогда берем элемент из левой половины
            left_index += 1
        else:
            array[array_index] = right_half[right_index]  # Иначе берем из правой
            right_index += 1
        array_index += 1  # Переходим к следующей позиции в исходном массиве

    # Добавляем элементы, пока они есть в левой половине
    while left_index < len(left_half):
        array[array_index] = left_half[left_index]
        left_index += 1
        array_index += 1

    # Добавляем элементы, пока они есть в правой половине
    while right_index < len(right_half):
        array[array_index] = right_half[right_index]
        right_index += 1
        array_index += 1

lst = [7, 5, 1, 6, 9, 13, 3, 4]

merge_sort(lst)
print(lst)