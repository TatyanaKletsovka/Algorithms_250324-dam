class Stack:
    def __init__(self):
        self.stack = []

    def empty(self):
        """Проверяет, пуст ли стек."""
        return len(self.stack) == 0

    def push(self, data):
        """Добавляет элемент на вершину стека."""
        self.stack.append(data)

    def pop(self):
        """Удаляет элемент с вершины стека и возвращает его."""
        if not self.empty():
            return self.stack.pop()
        else:
            return "Стек пуст!"

    def peek(self):
        """Возвращает элемент на вершине стека, не удаляя его."""
        if not self.empty():
            return self.stack[-1]
        else:
            return "Стек пуст!"

    def search(self, element):
        """Находит элемент в стеке и возвращает его позицию от вершины."""
        try:
            # Индекс элемента от начала
            index_from_bottom = self.stack.index(element)
            # Позиция от вершины стека
            position_from_top = len(self.stack) - self.stack.index(element)
            return position_from_top
        except ValueError:
            return -1  # Возвращает -1, если элемент не найден




