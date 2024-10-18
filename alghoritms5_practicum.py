# # ------------------------------------------------------------
# # Recursion
#
#
#
# def merge_sort(arr):
#     if len(arr) > 1:
#         # Находим середину массива
#         mid = len(arr) // 2
#         left_half = arr[:mid]
#         right_half = arr[mid:]
#
#         # Рекурсивно сортируем каждую половину
#         merge_sort(left_half)
#         merge_sort(right_half)
#
#         # Сливаем отсортированные половины
#         merge(arr, left_half, right_half)
#
# def merge(arr, left_half, right_half):
#     i = j = k = 0
#
#     # Сливаем два подмассива в один
#     while i < len(left_half) and j < len(right_half):
#         if left_half[i] < right_half[j]:
#             arr[k] = left_half[i]
#             i += 1
#         else:
#             arr[k] = right_half[j]
#             j += 1
#         k += 1
#
#     # Копируем оставшиеся элементы левого подмассива (если есть)
#     while i < len(left_half):
#         arr[k] = left_half[i]
#         i += 1
#         k += 1
#
#     # Копируем оставшиеся элементы правого подмассива (если есть)
#     while j < len(right_half):
#         arr[k] = right_half[j]
#         j += 1
#         k += 1
#
# # Пример использования
# arr = [5, 4, 3, 2, 1]
# # arr = ["banana", "apple", "orange", "grape"]
# merge_sort(arr)
# print("Отсортированный массив:", arr)
#
#
#
#
# # ------------------------------------------------------------
# # Iterative
#
#
#
# # def merge_sort_iterative(arr):
# #     # Начальная длина подмассивов для слияния - 1 (каждый элемент считается отсортированным)
# #     width = 1
# #     n = len(arr)
# #
# #     # Увеличиваем ширину подмассива на каждом этапе (вдвое)
# #     while width < n:
# #         # Проходим по массиву и сливаем подмассивы длиной width
# #         for i in range(0, n, 2 * width):
# #             left = arr[i:i + width]
# #             right = arr[i + width:i + 2 * width]
# #             arr[i:i + 2 * width] = merge(left, right)
# #
# #         # Увеличиваем размер подмассива
# #         width *= 2
# #
# #
# # def merge(left, right):
# #     result = []
# #     i = j = 0
# #
# #     # Слияние двух отсортированных подмассивов
# #     while i < len(left) and j < len(right):
# #         if left[i] < right[j]:
# #             result.append(left[i])
# #             i += 1
# #         else:
# #             result.append(right[j])
# #             j += 1
# #
# #     # Добавляем оставшиеся элементы
# #     result.extend(left[i:])
# #     result.extend(right[j:])
# #
# #     return result
# #
# #
# # # Пример использования
# # arr = [5, 4, 3, 2, 1]
# # merge_sort_iterative(arr)
# # print("Отсортированный массив:", arr)
#
#
#
#
# # ------------------------------------------------------------
# # count + merge
#
#
# #
# # def merge_sort(arr):
# #     if len(arr) > 1:
# #         # Находим середину массива
# #         mid = len(arr) // 2
# #         left_half = arr[:mid]
# #         right_half = arr[mid:]
# #
# #         # Рекурсивно сортируем каждую половину и возвращаем количество инверсий
# #         inv_count = merge_sort(left_half) + merge_sort(right_half)
# #
# #         # Сливаем отсортированные половины и добавляем количество инверсий
# #         inv_count += merge(arr, left_half, right_half)
# #
# #         return inv_count
# #     return 0
# #
# # def merge(arr, left_half, right_half):
# #     i = j = k = 0
# #     inv_count = 0
# #
# #     # Сливаем два подмассива в один
# #     while i < len(left_half) and j < len(right_half):
# #         if left_half[i] <= right_half[j]:
# #             arr[k] = left_half[i]
# #             i += 1
# #         else:
# #             # Когда элемент из правой половины меньше элемента из левой, значит есть инверсии
# #             arr[k] = right_half[j]
# #             inv_count += (len(left_half) - i)  # Все оставшиеся элементы в left_half больше
# #             j += 1
# #         k += 1
# #
# #     # Копируем оставшиеся элементы левого подмассива (если есть)
# #     while i < len(left_half):
# #         arr[k] = left_half[i]
# #         i += 1
# #         k += 1
# #
# #     # Копируем оставшиеся элементы правого подмассива (если есть)
# #     while j < len(right_half):
# #         arr[k] = right_half[j]
# #         j += 1
# #         k += 1
# #
# #     return inv_count
# #
# # # Пример использования
# # arr = [5, 4, 3, 2, 1]
# # inversion_count = merge_sort(arr)
# # print("Отсортированный массив:", arr)
# # print("Количество инверсий:", inversion_count)
# #
#
#
# # ------------------------------------------------------------
# # count
#
#
# # def inv(arr):
# #     n = len(arr)
# #     count = 0
# #     for i in range(n):
# #         for j in range(i + 1, n):
# #             if arr[i] > arr[j]:
# #                 count += 1
# #     return count
# #
# # print("Количество:", inv([5, 4, 3, 2, 1]))
#
#
#
# # ------------------------------------------------------------
# # max array
#
#
# #
# # def max_subarray_sum(arr):
# #     # Инициализируем переменные
# #     max_so_far = arr[0]
# #     max_ending_here = arr[0]
# #
# #     for i in range(1, len(arr)):
# #         # Обновляем max_ending_here
# #         current = arr[i]
# #         group = max_ending_here + arr[i]
# #         max_ending_here = max(current, group)
# #
# #         # Обновляем max_so_far
# #         max_so_far = max(max_so_far, max_ending_here)
# #
# #     return max_so_far
# #
# #
# # # Пример использования
# # arr = [2, -3, 1, 5, -6, 9]
# # result = max_subarray_sum(arr)
# # print("Максимальная сумма смежных элементов:", result)  # Вывод: 9
#
#
#
#
#
# # ------------------------------------------------------------
# # Пусть строки сортируются по длине, а если она одинаковая, то лексикографически
#
#
#
# def merge_sort(arr):
#     if len(arr) > 1:
#         # Находим середину массива
#         mid = len(arr) // 2
#         left_half = arr[:mid]
#         right_half = arr[mid:]
#
#         # Рекурсивно сортируем каждую половину
#         merge_sort(left_half)
#         merge_sort(right_half)
#
#         # Сливаем отсортированные половины
#         merge(arr, left_half, right_half)
#
# def merge(arr, left_half, right_half):
#     i = j = k = 0
#
#     # Сливаем два подмассива в один
#     while i < len(left_half) and j < len(right_half):
#         # Сравниваем по длине, затем лексикографически
#         if len(left_half[i]) < len(right_half[j]) or (len(left_half[i]) == len(right_half[j]) and left_half[i] < right_half[j]):
#             arr[k] = left_half[i]
#             i += 1
#         else:
#             arr[k] = right_half[j]
#             j += 1
#         k += 1
#
#     # Копируем оставшиеся элементы левого подмассива (если есть)
#     while i < len(left_half):
#         arr[k] = left_half[i]
#         i += 1
#         k += 1
#
#     # Копируем оставшиеся элементы правого подмассива (если есть)
#     while j < len(right_half):
#         arr[k] = right_half[j]
#         j += 1
#         k += 1
#
# # Пример использования
# string_list = ["cherry", "banana", "apple", "grape", "fig", "kiwi"]
# merge_sort(string_list)
# print("Отсортированный список строк:", string_list)
