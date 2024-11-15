class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            # Если список пустой, создаём первый узел, который ссылается сам на себя
            self.head = new_node
            new_node.next = self.head
        else:
            # Ищем последний узел
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            # Добавляем новый узел в конец и обновляем ссылки
            temp.next = new_node
            new_node.next = self.head

    def print_list(self):
        if not self.head:
            print("Список пуст")
            return

        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("... (циклический переход к началу)")

    def remove(self, key):
        if not self.head:
            print("Список пуст, нечего удалять")
            return

        # Если удаляемый элемент - головной узел
        if self.head.data == key:
            if self.head.next == self.head:
                # Если в списке только один элемент
                self.head = None
            else:
                # Если в списке больше одного элемента
                temp = self.head
                while temp.next != self.head:
                    temp = temp.next
                temp.next = self.head.next
                self.head = self.head.next
            return

        # Поиск узла перед узлом, который нужно удалить
        prev = None
        temp = self.head
        while temp.next != self.head:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if temp.data == key:
            prev.next = temp.next
        else:
            print(f"Элемент {key} не найден в списке")


# Пример использования
cll = CircularLinkedList()
cll.append(1)
cll.append(2)
cll.append(3)
cll.append(4)

print("Изначальный циклический список:")
cll.print_list()

# Удаление узла
cll.remove(3)
print("\nПосле удаления элемента 3:")
cll.print_list()