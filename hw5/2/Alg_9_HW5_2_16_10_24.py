import os

def merge_two_sorted_lists(list1, list2):
    # Сливает два отсортированных списка в один
    sorted_list = []
    i = j = 0

    # Пока в обоих списках есть элементы
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            sorted_list.append(list1[i])
            i += 1
        else:
            sorted_list.append(list2[j])
            j += 1

    # Добавляем оставшиеся элементы
    sorted_list.extend(list1[i:])
    sorted_list.extend(list2[j:])

    return sorted_list


def merge_files(file_list):
    # Принимает список файлов и сливает их содержимое в один отсортированный список
    merged_list = []

    # Читаем данные из каждого файла
    for file_name in file_list:
        with open(file_name, 'r') as file:
            # Считываем числа из файла и преобразуем их в список целых чисел
            numbers = list(map(int, file.read().split()))
            # Сливаем прочитанный список с уже существующим отсортированным списком
            merged_list = merge_two_sorted_lists(merged_list, numbers)

    return merged_list


def write_to_file(output_file, sorted_list):
    # Записывает отсортированный список в файл
    with open(output_file, 'w') as file:
        file.write(" ".join(map(str, sorted_list)))


# Пример использования программы:
if __name__ == "__main__":
    # Путь к директории с файлами
    directory = ''

    # Список файлов с отсортированными числами
    files = [
        os.path.join(directory, 'file1.txt'),
        os.path.join(directory, 'file2.txt'),
        os.path.join(directory, 'file3.txt')
    ]

    # Слияние содержимого файлов в один отсортированный список
    merged_result = merge_files(files)
    print(merged_result)

    # Запись результата в новый файл
    output_file = os.path.join(directory, 'merged_output.txt')
    write_to_file(output_file, merged_result)

    print(f"Данные успешно записаны в файл {output_file}")