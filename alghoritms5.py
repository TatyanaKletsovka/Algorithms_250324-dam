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



# lst = [5, 1, 3, 4]
# lst = [5, 3, 1]
# lst = [5, 6, 3, 4]
lst = []
# lst = [5]

merge_sort(lst)
print(lst)


