from collections import deque


def radix_sort(arr):
    # Определяем максимальное количество разрядов в числах
    max_digits = len(str(max(arr)))

    # Создаем 10 очередей для цифр от 0 до 9
    queues = [deque() for _ in range(10)]

    # Сортировка по каждому разряду
    for digit in range(max_digits):
        # Распределяем элементы по очередям в зависимости от текущего разряда
        for number in arr:
            # Извлекаем цифру текущего разряда
            current_digit = (number // (10 ** digit)) % 10
            queues[current_digit].append(number)

        # Сборка чисел из очередей в исходный массив
        arr.clear()
        for queue in queues:
            while queue:
                arr.append(queue.popleft())

    return arr


# Пример использования
arr = [82, 901, 100, 12, 150, 77, 55, 23]
sorted_arr = radix_sort(arr)
print("Отсортированный список:", sorted_arr)
