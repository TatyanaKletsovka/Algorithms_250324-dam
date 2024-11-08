class Stack:
    def __init__(self, elements=None):
        self.array = elements if elements is not None else []

    def empty(self):
        return len(self.array) == 0

    def push(self, element):
        self.array.append(element)

    def pop(self):
        if self.empty():
            raise IndexError("Попытка удаления из пустого стека")
        return self.array.pop()

    # Возвращение верхнего элемента, не удаляя его
    def peek(self):
        if self.empty():
            raise IndexError("Попытка удаления из пустого стека")
        return self.array[-1]

    # Поиск элемента в стеке
    def search(self, element):
        try:
            # Позиция с вершины стека
            return len(self.array) - self.array.index(element) - 1
        except ValueError:
            return -1

    def __str__(self):
        return f"Stack({self.array})"


# Пример использования
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print("Проверка стека на пустоту:", stack.empty())
print("Стек:", stack)
print("Верхний элемент:", stack.peek())
print("Удаление верхнего элемента:", stack.pop())
print("Поиск элемента 20:", stack.search(20))
print("Поиск элемента 40:", stack.search(40))
print("Стек:", stack)
