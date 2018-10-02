class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Queue:
    def __init__(self, head=None, tail=None):
        self.head = head    # remove from head
        self.tail = tail    # add things here

    def is_empty(self):
        return self.head is None

    def peek(self):
        if self.is_empty():
            return
        return self.head.data

    def add(self, data):
        node = Node(data)
        if self.tail is not None:
            self.tail.next = node

        self.tail = node
        if self.is_empty():
            self.head = node

    def remove(self):
        if self.is_empty():
            return
        data = self.head.data
        self.head = self.head.next
        if self.is_empty():
            self.tail = None
        return data


q = Queue()
q.add(3)
q.add(5)
q.add(20)
q.remove()
print(q.peek())
