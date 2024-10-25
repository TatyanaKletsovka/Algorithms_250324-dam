def quick_sort(arr):
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


numbers = [3, 9, 1, 4, 3, 9, 2, 0]
print(quick_sort(numbers))


# ------


def quick_sort_iterative(arr):
    if len(arr) <= 1:
        return arr
    stack = [(0, len(arr) - 1)] # для итеративного нужен доп. стек для памяти
    while stack:
        left, right = stack.pop() # с каждой итерации удаляет последний элемент (распоковка)
        if left >= right:         # здесь идет проверка границ
            continue

        pivot = arr[(left + right) // 2]
        low, high = left, right       #  устанавливаем переменные на границы текущего массива (подмассива)
        while low <= high:
            while arr[low] < pivot:
                low += 1
            while arr[high] > pivot:
                high -= 1
            if low <= high:
                arr[low], arr[high] = arr[high], arr[low]  # присваивание переменных на нужное место
                low += 1
                high -= 1
        if left < high:
            stack.append((left, high)) # добавляем границы подмассивов в стек
        if low < right:
            stack.append((low, right))
    return arr


numbers = [3, 9, 1, 4, 3, 9, 2, 0]
print(quick_sort_iterative(numbers))
