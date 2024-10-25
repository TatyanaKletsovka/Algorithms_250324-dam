def quick_sort(arr):
    stack = [(0, len(arr) - 1)]

    while stack:
        l, r = stack.pop()

        if l >= r:
            continue

        res = arr[(l + r) // 2]

        left = l
        right = r

        while left <= right:
            while arr[left] < res:
                left += 1
            while arr[right] > res:
                right -= 1

            if left <= right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1

        if l < right:
            stack.append((l, right))
        if left < r:
            stack.append((left, r))

    return arr

numbers = [5, 8, 1, 4, 3, 9, 2, 7]
print(quick_sort(numbers))
