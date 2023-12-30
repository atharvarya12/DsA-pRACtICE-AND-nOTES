class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def clear(self):
        trav = self.head
        while trav:
            next_node = trav.next
            trav.prev = trav.next = None
            trav.data = None
            trav = next_node
        self.head = self.tail = trav = None
        self.size = 0

    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def add(self, elem):
        self.add_last(elem)

    def add_last(self, elem):
        if self.is_empty():
            self.head = self.tail = Node(elem, None, None)
        else:
            self.tail.next = Node(elem, self.tail, None)
            self.tail = self.tail.next
        self.size += 1

    def add_first(self, elem):
        if self.is_empty():
            self.head = self.tail = Node(elem, None, None)
        else:
            self.head.prev = Node(elem, None, self.head)
            self.head = self.head.prev
        self.size += 1

    def peek_first(self):
        if self.is_empty():
            raise Exception("Empty list")
        return self.head.data

    def peek_last(self):
        if self.is_empty():
            raise Exception("Empty list")
        return self.tail.data

    def remove_first(self):
        if self.is_empty():
            raise Exception("Empty list")
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        if self.is_empty():
            self.tail = None
        else:
            self.head.prev = None
        return data

    def remove_last(self):
        if self.is_empty():
            raise Exception("Empty list")
        data = self.tail.data
        self.tail = self.tail.prev
        self.size -= 1
        if self.is_empty():
            self.head = None
        else:
            self.tail.next = None
        return data

    def remove_at(self, index):
        if index < 0 or index >= self.size:
            raise ValueError("Index out of bounds")
        i = 0
        trav = self.head
        while i != index:
            trav = trav.next
            i += 1
        return self.remove_node(trav)

    def remove(self, obj):
        trav = self.head
        while trav:
            if trav.data == obj:
                self.remove_node(trav)
                return True
            trav = trav.next
        return False

    def remove_node(self, node):
        if node.prev is None:
            return self.remove_first()
        elif node.next is None:
            return self.remove_last()
        else:
            node.next.prev = node.prev
            node.prev.next = node.next
            data = node.data
            node.data = None
            node.prev = node.next = None
            self.size -= 1
            return data

    def index_of(self, obj):
        index = 0
        trav = self.head
        while trav:
            if trav.data == obj:
                return index
            trav = trav.next
            index += 1
        return -1

    def contains(self, obj):
        return self.index_of(obj) != -1

    def __iter__(self):
        trav = self.head
        while trav:
            yield trav.data
            trav = trav.next

    def __str__(self):
        result = "[ "
        trav = self.head
        while trav:
            result += str(trav.data) + ", "
            trav = trav.next
        result += " ]"
        return result


# Example Usage:
dll = DoublyLinkedList()
dll.add_last(1)
dll.add_last(2)
dll.add_first(0)
dll.add_last(3)
dll.remove_first()
dll.remove_last()

print("Doubly Linked List:", dll)
