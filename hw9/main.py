# #Домашнее задание
# #1.Реализовать методы в MyLinkedList:
# #pushToTail(int data),
# #removeLast(),
# #get(int index)
#
#
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
# class MyLinkedList:
#     def __init__(self):
#         self.head = None
#         self.size = 0
#
#     def pushToTail(self, data):
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#         else:
#             current = self.head
#             while current.next:
#                 current = current.next
#             current.next = new_node
#         self.size += 1
#
#     def removeLast(self):
#         if not self.head:
#             return None
#         if not self.head.next:
#             removed_data = self.head.data
#             self.head = None
#         else:
#             current = self.head
#             while current.next and current.next.next:
#                 current = current.next
#             removed_data = current.next.data
#             current.next = None
#         self.size -= 1
#         return removed_data
#
#     def get(self, index):
#         if index < 0 or index >= self.size:
#             return None
#         current = self.head
#         for _ in range(index):
#             current = current.next
#         return current.data
#
# linked_list = MyLinkedList()
# linked_list.pushToTail(8)
# linked_list.pushToTail(16)
# linked_list.pushToTail(24)
#
#
# print([linked_list.get(i) for i in range(linked_list.size)])
#
#
# removed_element = linked_list.removeLast()
# print(f"Удалённый элемент: {removed_element}")
#
#
# print([linked_list.get(i) for i in range(linked_list.size)])








#2.Переделать односвязный список в двусвязный.
#Подсказка: подумать, как изменится класс MyLinkedList? Какое поле к нему добавится?
#Как это повлияет на реализованные операции для односвязного? Уменьшится ли сложность некоторых из них?

class DoubleNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def pushToTail(self, data):
        new_node = DoubleNode(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1

    def removeLast(self):
        if not self.head:
            return None
        if not self.head.next:
            removed_data = self.head.data
            self.head = None
            self.tail = None
        else:
            removed_data = self.tail.data
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1
        return removed_data

    def get(self, index):
        if index < 0 or index >= self.size:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data

linked_list = DoubleLinkedList()
linked_list.pushToTail(8)
linked_list.pushToTail(16)
linked_list.pushToTail(24)

print([linked_list.get(i) for i in range(linked_list.size)])

removed_element = linked_list.removeLast()
print(f"Удалённый элемент: {removed_element}")

print([linked_list.get(i) for i in range(linked_list.size)])