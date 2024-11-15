class Node:
    def __init__(self, data):
        self.data = data  # Данные узла
        self.next = None  # Ссылка на следующий узел
        self.prev = None  # Ссылка на предыдущий узел


class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Голова списка (первый узел)

    def append(self, data):
        new_node = Node(data)  # Создаем новый узел
        if not self.head:
            self.head = new_node  # Если список пуст, новый узел становится головой
            return
        last = self.head
        while last.next:  # Проходим к последнему узлу
            last = last.next
        last.next = new_node  # Присоединяем новый узел в конец
        new_node.prev = last  # Обновляем указатель на предыдущий узел

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node  # Если список пуст, новый узел становится головой
            return
        new_node.next = self.head  # Новый узел указывает на текущую голову
        self.head.prev = new_node  # Текущая голова указывает на новый узел как на предыдущий
        self.head = new_node  # Обновляем голову

    def delete(self, key):
        current = self.head
        while current:
            if current.data == key:
                if current.prev:  # Если узел не голова, обновляем указатель предыдущего узла
                    current.prev.next = current.next
                else:
                    self.head = current.next  # Если узел голова, обновляем голову
                if current.next:  # Если узел не последний, обновляем указатель следующего узла
                    current.next.prev = current.prev
                return
            current = current.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")


# Пример использования
dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.prepend(0)
dll.display()  # Вывод: 0 <-> 1 <-> 2 <-> 3 <-> None

dll.delete(2)
dll.display()  # Вывод: 0 <-> 1 <-> 3 <-> None
