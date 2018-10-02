class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        if self.head is None:
            self.head = Node(data)      # Head is now populated
            return
        current = self.head
        while current.next is not None:   # Keep going until last element
            current = current.next
        current.next = Node(data)       # Point to new Node

    def prepend(self, data):
        new_head = Node(data)           # new head with data
        new_head.next = self.head       # new head points to head
        self.head = new_head            # replacing head

    def delete_with_value(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next              # deleting head
            return

        current = self.head                         # start @ head
        while current.next is not None:
            if current.next.data == data:         # if data == data given stop
                current.next = current.next.next    # skip this node
                return
            current = current.next

    def count_nodes(self):
        if self.head is None:
            print 0
            return
        count = 1

        while self.head.next is not None:
            self.head = self.head.next
            count += 1

        print(count)


n1 = Node(1)
ll = LinkedList()
ll.count_nodes()
ll.insert(3)
ll.count_nodes()
ll.prepend(4)
ll.count_nodes()
ll.delete_with_value(3)
ll.count_nodes()

print(ll)
