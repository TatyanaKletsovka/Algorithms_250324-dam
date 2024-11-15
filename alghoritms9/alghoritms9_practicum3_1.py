class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def find_middle_and_after(self):
        slow = self.head
        fast = self.head

        # Используем два указателя для нахождения середины
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Возвращаем все элементы, начиная с середины
        result = []
        while slow:
            result.append(slow.data)
            slow = slow.next
        return result

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Пример использования
linked_list = MyLinkedList()
for i in [1, 2, 3, 4, 5]:
    linked_list.push(i)

print("Список:")
linked_list.print_list()

middle_and_after = linked_list.find_middle_and_after()
print("Центральный элемент и все элементы после него:", middle_and_after)
