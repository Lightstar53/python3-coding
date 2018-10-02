class Stack:
    def __init__(self, top=None):
        self.top = top

    def is_empty(self):
        return self.top is None

    def peek(self):
        if self.is_empty():
            return
        return self.top.data

    def push(self, data):
        node = Node(data)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.is_empty():
            return
        data = self.top.data
        self.top = self.top.next
        return data


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


s = Stack()
s.push(3)
s.push(5)
s.pop()
print(s.peek())