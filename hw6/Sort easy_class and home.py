'''In class'''


def quick_sort(arr):
    # middle_ind = len(arr) // 2
    # middle_el = arr[middle_ind]
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = []
    middle = []
    right = []
    for el in arr:
        if el < pivot:
            left.append(el)
        elif el > pivot:
            right.append(el)
        else:
            middle.append(el)
    return quick_sort(left) + middle + quick_sort(right)


numbers = [5, 8, 1, 4, 3, 9, 2, 7]
print(quick_sort(numbers))

'''At home:'''


def quick_sort1(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left = []
    middle = []
    right = []

    for el in arr:
        if el < pivot:
            left.append(el)
        elif el > pivot:
            right.append(el)
        else:
            middle.append(el)

    return quick_sort1(left) + middle + quick_sort1(right)


numbers = [5, 8, 1, 4, 3, 9, 2, 7]
print(quick_sort1(numbers))
