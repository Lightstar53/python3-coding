class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def insert(self, value):
        if value <= self.data:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)

    def contains(self, value):
        if value == self.data:
            return True
        elif value < self.data:
            if self.left is None:
                return False
            else:
                return self.left.contains(value)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(value)

    # Left, Root, Right
    def print_in_order(self):
        if self.left is not None:
            self.left.print_in_order()
        print(self.data)
        if self.right is not None:
            self.right.print_in_order()

    # Root, Left, Right
    def print_pre_order(self):
        print(self.data) # print root
        if self.left is not None:
            self.left.print_pre_order()
        if self.right is not None:
            self.right.print_pre_order()

    # Left, Right, Root
    def print_post_order(self):
        if self.left is not None:
            self.left.print_pre_order()
        if self.right is not None:
            self.right.print_pre_order()
        print(self.data)  # print root


n = Node(10, Node(5), Node(15))
n.insert(8)
print(n)
print(n.contains(3))
print(n.contains(5))
print(n.contains(8))
n.print_in_order()
print()
n.print_pre_order()
print()
n.print_post_order()