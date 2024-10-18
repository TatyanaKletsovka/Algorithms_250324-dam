from array import array

arr = [-2, -1, 1, 3, 5, 8, 11, 14, 15, 19]
# arr = [-4, -3, -2, -1, 1, 3, 5, 8, 11, 14]

def magic_index_iter(array):

    for index, value in enumerate(array):
        if index == value:
            return index
    return -1

# print(magic_index_iter(arr))

def magic_index_base_recur(array, min_index=0, max_index=None):
    if not max_index:
        max_index = len(array) - 1

    if min_index > max_index:
        return -1

    if array[min_index] == min_index:
        return min_index

    return magic_index_base_recur(array, min_index + 1, max_index)

# print((magic_index_base_recur(arr)))



def magic_index_effect_recur(array, min_index=0, max_index=None):
    if not max_index:
        max_index = len(array) - 1

    if min_index > max_index:
        return -1

    middle_index = (min_index + max_index) // 2

    if array[middle_index] == middle_index:
        return middle_index

    if array[middle_index] > middle_index:
        return magic_index_effect_recur(array, min_index, middle_index - 1)
    else:
        return magic_index_effect_recur(array, middle_index + 1, max_index)


print((magic_index_effect_recur(arr)))


[0, 1, 2, 3, 4, 5, 10, 9, 8, 7, 6]


# Найти максимальный элемент в массиве.
# Известно, что в таком массиве максимум находится по соседству с меньшими элементами, т.е.
# предыдущий и следующий за ним элементы гарантировано меньше искомого.
# Пример входного массива: array [0,1,2,3,4,5,10,9,8,7,6]
# max = 10;

array = [0,1,2,3,4,5,10,9,8,7,6]
array = [0,1,2,3,4,5,10]

def find_el_recursive(arr, start_el, end_el):
    if start_el == end_el:
        return arr[start_el]

    middle_el = (start_el + end_el) // 2

    if (middle_el == 0 or arr[middle_el - 1] < arr[middle_el]) and (middle_el == len(arr) - 1 or arr[middle_el] > arr[middle_el + 1]):
        return arr[middle_el]

    elif middle_el > 0 and arr[middle_el - 1] > arr[middle_el]:
        return find_el_recursive(arr, start_el, middle_el - 1)

    else:
        return find_el_recursive(arr, middle_el + 1, end_el)

def find_el(arr):
    return find_el_recursive(arr, 0, len(arr) - 1)


max_el = find_el(array)
print(f"Максимальный элемент: {max_el}")
