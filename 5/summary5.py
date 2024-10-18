# ------------------------------------------------------------
# count


# def inv(arr):
#     n = len(arr)
#     count = 0
#     for i in range(n):
#         for j in range(i + 1, n):
#             previous_el = arr[i]
#             next_el = arr[j]
#             if previous_el > next_el:
#                 count += 1
#     return count
#
# print("Количество:", inv([5, 4, 3, 2, 1]))





# ------------------------------------------------------------
# count + merge



def merge_sort(arr):
    if len(arr) > 1:
        # Находим середину массива
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Рекурсивно сортируем каждую половину и возвращаем количество инверсий
        inv_count = merge_sort(left_half) + merge_sort(right_half)

        # Сливаем отсортированные половины и добавляем количество инверсий
        inv_count += merge(arr, left_half, right_half)

        return inv_count
    return 0

def merge(arr, left_half, right_half):
    i = j = k = 0
    inv_count = 0

    # Сливаем два подмассива в один
    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            # Когда элемент из правой половины меньше элемента из левой, значит есть инверсии
            arr[k] = right_half[j]
            inv_count += (len(left_half) - i)  # Все оставшиеся элементы в left_half больше
            j += 1
        k += 1

    # Копируем оставшиеся элементы левого подмассива (если есть)
    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1

    # Копируем оставшиеся элементы правого подмассива (если есть)
    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1

    return inv_count

# Пример использования
arr = [5, 4, 3, 2, 1]
inversion_count = merge_sort(arr)
print("Отсортированный массив:", arr)
print("Количество инверсий:", inversion_count)

