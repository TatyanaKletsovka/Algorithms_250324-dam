numbers = [1, 2, 3]
# numbers = []

print(len(numbers))
print(numbers.__len__())

# if numbers:
#     is_empty = True
#     print('not empty')
#     print(is_empty)


is_empty = bool(numbers)
print(is_empty)


from collections import deque

import queue

q = deque

