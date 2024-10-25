def merge_files(file_list, output_file):

    combined_data = []
    for file_name in file_list:
        with open(file_name, 'r') as file:
            numbers = list(map(int, filter(lambda x: x.strip() != '', file.readlines())))
            combined_data.extend(numbers)


    merge_sort(combined_data)


    with open(output_file, 'w') as output:
        for number in combined_data:
            output.write(f"{number}\n")


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        merge_sort(left_half)
        merge_sort(right_half)

        merge(arr, left_half, right_half)


def merge(arr, left_half, right_half):
    left_ind = right_ind = arr_ind = 0
    while left_ind < len(left_half) and right_ind < len(right_half):
        if left_half[left_ind] < right_half[right_ind]:
            arr[arr_ind] = left_half[left_ind]
            left_ind += 1
        else:
            arr[arr_ind] = right_half[right_ind]
            right_ind += 1
        arr_ind += 1


    while left_ind < len(left_half):
        arr[arr_ind] = left_half[left_ind]
        left_ind += 1
        arr_ind += 1


    while right_ind < len(right_half):
        arr[arr_ind] = right_half[right_ind]
        right_ind += 1
        arr_ind += 1


if __name__ == "__main__":
    file_list = ['sorted_file1.txt', 'sorted_file2.txt', 'sorted_file3.txt']
    output_file = 'merged_output.txt'
    merge_files(file_list, output_file)
