# Функция для слияния двух подмассивов и подсчета инверсий
def merge_and_count(arr, temp_arr, left, mid, right):
    i = left
    j = mid + 1
    k = left
    inv_count = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            temp_arr[k] = arr[j]
            inv_count += (mid - i + 1)
            j += 1
        k += 1

    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1

    for i in range(left, right + 1):
        arr[i] = temp_arr[i]

    return inv_count

def merge_sort_and_count(arr, temp_arr, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2


        inv_count += merge_sort_and_count(arr, temp_arr, left, mid)
        inv_count += merge_sort_and_count(arr, temp_arr, mid + 1, right)

        inv_count += merge_and_count(arr, temp_arr, left, mid, right)

    return inv_count

def count_inversions(arr):
    temp_arr = [0] * len(arr)
    return merge_sort_and_count(arr, temp_arr, 0, len(arr) - 1)

arr1 = [8, 4, 2, 1]
print("Число инверсий в массиве:", count_inversions(arr1))

arr2 = [3, 1, 2]
print("Число инверсий в массиве:", count_inversions(arr2))

# Реализуйте программу, которая принимает несколько файлов, каждый из которых содержит отсортированный список чисел, и объединяет их в один отсортированный файл,
# используя сортировку слиянием.

import heapq

def read_numbers_from_file(filename):
    try:
        with open(filename, 'r') as file:
            return list(map(int, file.readlines()))
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден. Проверьте путь к файлу.")
        return []

def write_numbers_to_file(filename, numbers):
    with open(filename, 'w') as file:
        for number in numbers:
            file.write(f"{number}\n")

def merge_sorted_files(input_files, output_file):
    sorted_lists = [read_numbers_from_file(file) for file in input_files]

    # Объединение списков с помощью кучи (heapq.merge)
    merged = heapq.merge(*sorted_lists)

    write_numbers_to_file(output_file, merged)

input_files = ['C:/Users/risch/Documents/file1.txt',
               'C:/Users/risch/Documents/file2.txt',
               'C:/Users/risch/Documents/file3.txt']
output_file = 'C:/Users/risch/Documents/merged_output.txt'
merge_sorted_files(input_files, output_file)

print(f"Данные из файлов {input_files} объединены и отсортированы в {output_file}")
