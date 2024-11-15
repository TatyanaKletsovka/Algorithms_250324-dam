class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Ссылка на следующий узел


class MyLinkedList:
    def __init__(self):
        self.head = None  # Изначально список пуст
        self.length = 0  # Длина списка

    # Добавить элемент в начало списка
    def pushToHead(self, data):
        new_node = Node(data)
        new_node.next = self.head  # Новый узел указывает на старую голову
        self.head = new_node  # Новый узел становится головой
        self.length += 1

    # Добавить элемент по индексу
    def pushToIndex(self, index, data):
        if index < 0 or index > self.length:
            raise IndexError("Неверный индекс")

        new_node = Node(data)

        # Если индекс 0, просто добавляем в начало
        if index == 0:
            self.pushToHead(data)
            return

        current = self.head
        for _ in range(index - 1):
            current = current.next

        # Вставляем новый узел
        new_node.next = current.next
        current.next = new_node
        self.length += 1

    # Удалить первый элемент
    def removeFirst(self):
        if self.head is None:
            raise RuntimeError("Список пуст")

        self.head = self.head.next  # Голова теперь указывает на следующий элемент
        self.length -= 1

    # Удалить элемент по индексу
    def remove(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Неверный индекс")

        # Если индекс 0, просто удаляем первый элемент
        if index == 0:
            self.removeFirst()
            return

        current = self.head
        for _ in range(index - 1):
            current = current.next

        # Удаляем узел, изменяя ссылку предыдущего узла
        current.next = current.next.next
        self.length -= 1

    # Получить размер списка
    def size(self):
        return self.length

    # Напечатать все элементы списка
    def print(self):
        if self.head is None:
            print("Список пуст")
            return

        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")  # Конец списка


# Пример использования
my_list = MyLinkedList()
my_list.pushToHead(10)
my_list.pushToHead(20)
my_list.pushToIndex(1, 15)
my_list.pushToHead(30)
print("Список после вставки элементов:")
my_list.print()

my_list.remove(2)
print("\nСписок после удаления элемента с индексом 2:")
my_list.print()

my_list.removeFirst()
print("\nСписок после удаления первого элемента:")
my_list.print()

print("\nРазмер списка:", my_list.size())
