def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_index, right_index = 0, 0


    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


if __name__ == "__main__":
    test_cases = [
        [38, 27, 43, 3, 9, 82, 10],  # обычный массив
        [],                          # пустой массив
        [1, 1, 1, 1],               # массив с одинаковыми данными
        [5, 4, 3, 2, 1],            # массив, отсортированный в обратном порядке
        [2, 3, 1],                  # нечетное количество элементов
        [2, 1, 3, 4],               # четное количество элементов
    ]

    for i, test in enumerate(test_cases):
        sorted_array = merge_sort(test)
        print(f"Test case {i + 1}: {sorted_array}")
