'''Имея два отсортированных массива размера m и n соответственно, вам нужно найти элемент,
который будет находиться на k-й позиции в конечном отсортированном массиве.
Массив 1 - 100 112 256 349 770
Массив 2 - 72 86 113 119 265 445 892
к = 7
Вывод : 256
Окончательный отсортированный массив - 72, 86, 100, 112, 113, 119, 256, 265, 349, 445, 770, 892
7-й элемент этого массива равен 256'''


def find_k_element(arr1, arr2, k):
    len1, len2 = len(arr1), len(arr2)

    if len1 == 0:
        return arr2[k - 1]
    if len2 == 0:
        return arr1[k - 1]

    if k == 1:
        return min(arr1[0], arr2[0])

    i = min(len1, k // 2)
    j = min(len2, k // 2)

    if arr1[i - 1] < arr2[j - 1]:
        return find_k_element(arr1[i:], arr2, k - i)
    else:
        return find_k_element(arr1, arr2[j:], k - j)


array1 = [100, 112, 256, 349, 770]
array2 = [72, 86, 113, 119, 265, 445, 892]
k = 7

kth_element = find_k_element(array1, array2, k)
print(f"{k}-й элемент в объединенном массиве: {kth_element}")
