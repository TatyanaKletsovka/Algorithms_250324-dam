class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Ссылка на следующий узел
        self.prev = None  # Ссылка на предыдущий узел

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None  # Изначально список пуст

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            # Если список пуст, создаём первый узел, который ссылается сам на себя
            self.head = new_node
            new_node.next = self.head
            new_node.prev = self.head
        else:
            # Если список не пустой, вставляем новый узел в конец
            tail = self.head.prev  # Последний узел
            tail.next = new_node
            new_node.prev = tail
            new_node.next = self.head
            self.head.prev = new_node

    def print_list(self):
        if not self.head:
            print("Список пуст")
            return

        temp = self.head
        while True:
            print(temp.data, end=" <=> ")
            temp = temp.next
            if temp == self.head:
                break
        print("... (циклический переход к началу)")

    def remove(self, key):
        if not self.head:
            print("Список пуст, нечего удалять")
            return

        # Если нужно удалить головной элемент
        if self.head.data == key:
            if self.head.next == self.head:
                # Если в списке только один элемент
                self.head = None
            else:
                # Если элементов больше одного
                tail = self.head.prev
                self.head = self.head.next
                self.head.prev = tail
                tail.next = self.head
            return

        # Поиск и удаление узла с нужным значением
        temp = self.head
        while True:
            if temp.data == key:
                break
            temp = temp.next
            if temp == self.head:
                print(f"Элемент {key} не найден в списке")
                return

        # Переназначение указателей для удаления узла
        temp.prev.next = temp.next
        temp.next.prev = temp.prev

# Пример использования
cll = CircularDoublyLinkedList()
cll.append(1)
cll.append(2)
cll.append(3)
cll.append(4)

print("Изначальный циклический двусвязный список:")
cll.print_list()

# Удаление элемента
cll.remove(3)
print("\nПосле удаления элемента 3:")
cll.print_list()
