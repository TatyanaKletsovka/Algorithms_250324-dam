# a = [1, 3, 4, 8]
# b = [2, 5, 6, 9, 10, 12]
#
# result = []
# #
# i = 0
# j = 0
# while i < len(a) and j < len(b):
#     if a[i] < b[j]:
#         result.append(a[i])
#         i += 1
#     else:
#         result.append(b[j])
#         j += 1


# for i, v in enumerate(a):
#     # print("-----")
#     a_el = v
#     b_el = b[i]
#
#     a.append(v)
#     b.append(b[i])


# for i, v in enumerate(b):
#     # print("-----")
#     a.append(b)

# iter_obj = a.__iter__()
# print(iter_obj)
# print(iter_obj.__next__())
# print(iter_obj.__next__())
# print(iter_obj.__next__())
# print(iter_obj.__next__())
# # print(iter_obj.__next__())



# [5, 8, 1, 4, 3, 9, 2, 7]
#
# [1, 2, 5, 8, 4, 3, 9, 7]
#
# 5
#
# [2]
#
# [9, 8, 7]



def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    print()
    left = []
    right = []
    middle = []
    for el in arr:
        if el < pivot:
            left.append(el)
        elif el > pivot:
            right.append(el)
        else:
            middle.append(el)
    return quick_sort(left) + middle + quick_sort(right)



numbers = [5, 8, 3, 1, 4, 3, 9, 2, 1, 7]
# numbers = [5, 8, 3, 1]
print(quick_sort(numbers))


# i = j = k = 0
# j += 1
# print(i, j, k)
#
# left = right = middle = []
# left = [1]
# left.append(1)
# print(left, right, middle)
