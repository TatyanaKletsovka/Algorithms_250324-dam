#1.Переписать самостоятельно то, что написали во время занятия:
# заново написать быструю сортировку, опираясь на текстовое описание.
#Выбираем опорный элемент из массива. Как правило, это средний элемент.
#Делим массив на 2 подмассива. Элементы, которые меньше опорного,
# и элементы, которые больше опорного.
#Рекурсивно применяем сортировку к обоим подмассивам.
#В результате массивы будут делиться до тех пор, пока не останется один элемент,
# который потом отсортируется.

def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)


array = [3, 6, 8, 10, 1, 2, 1]
sorted_array = quicksort(array)
print(sorted_array)



#Реализовать Quicksort используя итерационный подход.

def quicksort_iterative(arr):
    stack = [(0, len(arr) - 1)]

    while stack:
        low, high = stack.pop()
        if low < high:
            pivot_index = partition(arr, low, high)

            stack.append((low, pivot_index - 1))
            stack.append((pivot_index + 1, high))

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


array = [3, 6, 8, 10, 1, 2, 1]
quicksort_iterative(array)
print(array)
