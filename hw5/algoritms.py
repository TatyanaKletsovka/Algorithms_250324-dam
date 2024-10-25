def merge_sorted_lists(lists):
    result = []
    indices = [0] * len(lists)

    while True:
        min_val = None
        min_list_index = -1

        for i in range(len(lists)):
            if indices[i] < len(lists[i]):
                if min_val is None or lists[i][indices[i]] < min_val:
                    min_val = lists[i][indices[i]]
                    min_list_index = i

        if min_val is None:
            break

        result.append(min_val)
        indices[min_list_index] += 1

    return result


def merge_sorted_files(input_files, output_file):
    # Читаем данные из всех файлов
    sorted_lists = []
    for file in input_files:
        with open(file, 'r') as f:
            sorted_lists.append([int(line.strip()) for line in f])

    merged_list = merge_sorted_lists(sorted_lists)

    with open(output_file, 'w') as out_file:
        for number in merged_list:
            out_file.write(f"{number}\n")


input_files = ['file1.txt', 'file2.txt', 'file3.txt']  # список входных файлов с числами
output_file = 'merged_output.txt'  # файл для записи результата

merge_sorted_files(input_files, output_file)

