class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.empty():
            return None
        return self.items.pop()

    def peek(self):
        if self.empty():
            return None
        return self.items[-1]

    def search(self, element):
        # с вершины
        if element in self.items:
            # от конца стека
            return len(self.items) - self.items.index(element) - 1
        return -1

    def empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def __str__(self):
        return f'Stack {self.items}'


stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)

print(stack)


print("Peek:", stack.peek())


print("Pop:", stack.pop())
print(stack)


print("Search 20:", stack.search(20))
print("Search 20:", stack.search(30))
print("Search 40:", stack.search(60))


print("Is empty:", stack.empty())
