class Stack:
    def __init__(self):
        self.res = []

    def empty(self):
        # return len(self.res) == 0
        return not bool(self.res)

    def push(self, element):
        self.res.append(element)

    def pop(self):
        if self.empty():
            return "Стек пуст"
        return self.res.pop()

    def peek(self):
        if self.empty():
            return "Стек пуст"
        return self.res[-1]

    def search(self, element):
        if element in self.res:
            return len(self.res) - self.res.index(element) - 1
        return -1

res = Stack()
print("empty", res.empty())

res.push(10)
res.push(20)
res.push(30)

print("peek:", res.peek())
print("search 10:", res.search(10))
print("Ищем элемент 20:", res.search(20))
print("empty:", res.empty())

print("pop 1:", res.pop())
print("pop 2:", res.pop())
print("pop 3:", res.pop())
print("empty:", res.empty())
