# Функция для слияния двух отсортированных списков
def merge(left, right):
    result = []  # результат слияния двух подсписков
    i = j = 0  # указатели на текущие элементы в списках left и right

    # Пока есть элементы в обоих подсписках
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])  # добавляем меньший элемент в результат
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Добавляем оставшиеся элементы из left или right
    result.extend(left[i:])
    result.extend(right[j:])

    return result

# Рекурсивная функция для сортировки слиянием
def merge_sort(arr):
    # Базовый случай: если длина массива <= 1, он уже отсортирован
    if len(arr) <= 1:
        return arr

    # Находим середину массива
    mid = len(arr) // 2

    # Рекурсивно делим массив на две части
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Сливаем две отсортированные части
    return merge(left, right)


import random
import csv  # Импорт библиотеки csv для работы с CSV файлами

# Функция для генерации массива случайных чисел
def generate_random_array(length, min_value=0, max_value=100):
    return [random.randint(min_value, max_value) for _ in range(length)]

array_length = 11
random_array = generate_random_array(array_length, 1, 100)
print("Случайный массив:", random_array)

sorted_arr = merge_sort(random_array)
print("Отсортированный массив:", sorted_arr)
# Функция для записи отсортированного массива в CSV файл
def write_array_to_csv(arr, filename='sorted_array.csv'):
    """Записывает массив в CSV файл с разделителем-запятой."""
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(arr)
# Запись отсортированного массива в CSV файл
write_array_to_csv(sorted_arr, 'sorted_array1.csv')
print("Отсортированный массив был записан в 'sorted_array1.csv'")
