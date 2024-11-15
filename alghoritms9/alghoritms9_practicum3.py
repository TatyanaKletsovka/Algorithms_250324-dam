class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Ссылка на следующий узел


class MyCircularLinkedList:
    def __init__(self):
        self.head = None

    def pushToHead(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head  # Устанавливаем петлю
        else:
            new_node.next = self.head
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def findCenterAndRest(self):
        if not self.head:
            return []

        slow = self.head
        fast = self.head

        # Используем два указателя, чтобы найти центр
        while fast and fast.next != self.head:
            slow = slow.next
            fast = fast.next.next

        # После нахождения центра, собираем все элементы
        result = []
        current = slow
        while True:
            result.append(current.data)
            current = current.next
            if current == slow:  # Если снова вернулись к центру, заканчиваем
                break
        return result


# Пример для кругового списка:
my_circular_list = MyCircularLinkedList()
my_circular_list.pushToHead(5)
my_circular_list.pushToHead(4)
my_circular_list.pushToHead(3)
my_circular_list.pushToHead(2)
my_circular_list.pushToHead(1)

center_and_rest_circular = my_circular_list.findCenterAndRest()
print(center_and_rest_circular)
