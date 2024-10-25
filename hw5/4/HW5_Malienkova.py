#2. Реализуйте программу, которая принимает несколько файлов,
# каждый из которых содержит отсортированный список чисел, и объединяет их
# в один отсортированный файл, используя сортировку слиянием.
import os

with open('file1.txt', 'w') as f:
    f.write('\n'.join(map(str, [1, 3, 5, 7, 9])))

with open('file2.txt', 'w') as f:
    f.write('\n'.join(map(str, [2, 4, 6, 8, 10])))

with open('file3.txt', 'w') as f:
    f.write('\n'.join(map(str, [11, 13, 15, 17, 19])))


def merge_sorted_files(input_files, output_file):
    for file in input_files:
        if not os.path.isfile(file):
            raise FileNotFoundError(f"Файл не найден: {file}")

    sorted_lists = []

    for file in input_files:
        with open(file, 'r') as f:
            sorted_list = [int(line.strip()) for line in f]
            sorted_lists.append(sorted_list)

    merged_list = merge_sorted_lists(sorted_lists)

    with open(output_file, 'w') as f:
        for number in merged_list:
            f.write(f"{number}\n")


def merge_sorted_lists(sorted_lists):
    merged = []
    indices = [0] * len(sorted_lists)

    while True:
        min_value = None
        min_index = -1

        for i in range(len(sorted_lists)):
            if indices[i] < len(sorted_lists[i]):
                if min_value is None or sorted_lists[i][indices[i]] < min_value:
                    min_value = sorted_lists[i][indices[i]]
                    min_index = i

        if min_index == -1:
            break

        merged.append(min_value)
        indices[min_index] += 1

    return merged


input_files = ['file1.txt', 'file2.txt', 'file3.txt']
output_file = 'merged_output.txt'

try:
    merge_sorted_files(input_files, output_file)
    print(f"Файлы успешно объединены в '{output_file}'.")
except FileNotFoundError as e:
    print(e)
