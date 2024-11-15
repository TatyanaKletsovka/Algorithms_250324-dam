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

    # Метод для создания петли (цикла) в списке
    def createLoop(self, index):
        if index < 0 or index >= self.length:
            print("Неверный индекс для создания петли")
            return

        # Ищем узел с указанным индексом
        loop_node = self.head
        for _ in range(index):
            loop_node = loop_node.next

        # Ищем последний узел списка
        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        # Делаем последний узел указывать на узел с данным индексом
        last_node.next = loop_node

    # Метод для проверки наличия цикла
    def hasLoop(self):
        slow = self.head  # Указатель черепахи
        fast = self.head  # Указатель зайца

        while fast and fast.next:
            slow = slow.next  # Шаг черепахи
            fast = fast.next.next  # Шаг зайца

            if slow == fast:  # Если черепаха и заяц встретились — есть цикл
                return True

        return False  # Цикл не найден

    # Напечатать все элементы списка
    def print(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Пример использования
my_list = MyLinkedList()
my_list.pushToHead(10)
my_list.pushToHead(20)
my_list.pushToHead(30)
my_list.pushToHead(40)
my_list.pushToHead(50)

# Создание петли на 2-ом элементе (индекс 1)
my_list.createLoop(1)

# Проверка наличия цикла
print("Есть ли цикл в списке?", my_list.hasLoop())
