#Реализовать стек и его операции на основе массива.
#empty  — проверка стека на наличие в нем элементов,
#push  — операция вставки нового элемента,
#pop  — операция удаления нового элемента.

class Stack:
    def __init__(self):
        self.stack = []

    def empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.empty():
            return self.stack.pop()
        else:
            print("Стек пуст")
            return None


s = Stack()
print(s.empty())   # True
s.push(3)
s.push(6)
print(s.empty())   # False
print(s.pop())     # 6
print(s.pop())     # 3
print(s.pop())     # None, так как стек уже пуст


print("=========================")


#Реализовать нижеперечисленные операции самостоятельно для структуры Стек:
#peek() – Возвращает элемент c вершины стека, но не удаляет его.
#search(element) -  Определяет, существует ли объект в стеке. Если элемент найден,
# возвращает позицию элемента с вершины стека. В противном случае он возвращает -1.


class Stack:
    def __init__(self):
        self.stack = []

    def empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.empty():
            return self.stack.pop()
        else:
            print("Стек пуст")
            return None

    def peek(self):
        if not self.empty():
            return self.stack[-1]
        else:
            print("Стек пуст")
            return None

    def search(self, element):
        if element in self.stack:
            return len(self.stack) - self.stack.index(element) - 1
        else:
            return -1


s = Stack()
s.push(6)
s.push(9)
print(s.peek())      # 9
print(s.search(6))  # 1 (позиция от вершины)
print(s.search(12))  # -1 (элемент не найден)
print(s.pop())       # 9
print(s.peek())      # 6

