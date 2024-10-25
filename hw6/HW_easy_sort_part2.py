def quick_sort_it(arr):
    stack = [(0, len(arr) - 1)]

    while stack:
        start, end = stack.pop()

        if start >= end:
            continue

        pivot = arr[(start + end) // 2]

        left = start
        right = end

        while left <= right:
            while arr[left] < pivot:
                left += 1
            while arr[right] > pivot:
                right -= 1
            if left <= right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1

        if start < right:
            stack.append((start, right))
        if left < end:
            stack.append((left, end))

    return arr


numbers = [5, 8, 1, 4, 3, 9, 2, 7]
print(quick_sort_it(numbers))