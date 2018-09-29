# Min Heap implemented as list
class MinIntHeap:
    def __init__(self, capacity=10, size=0):
        self.capacity = capacity
        self.size = size
        self.items = [None] * capacity

    @staticmethod
    def get_left_child_index(parent_index):
        return 2 * parent_index + 1

    @staticmethod
    def get_right_child_index(parent_index):
        return 2 * parent_index + 2

    @staticmethod
    def get_parent_index(child_index):
        return (child_index - 1) // 2

    def has_left_child(self, index):
        return self.get_left_child_index(index) < self.size

    def has_right_child(self, index):
        return self.get_right_child_index(index) < self.size

    def has_parent(self, index):
        return self.get_parent_index(index) >= 0

    def left_child(self, index):
        return self.items[self.get_left_child_index(index)]

    def right_child(self, index):
        return self.items[self.get_right_child_index(index)]

    def parent(self, index):
        return self.items[self.get_parent_index(index)]

    def swap(self, index_one, index_two):
        temp = self.items[index_one]
        self.items[index_one] = self.items[index_two]
        self.items[index_two] = temp

    def ensure_extra_capacity(self):
        if self.size == self.capacity:
            # double size of array? does this already i think?
            self.capacity *= 2

    def peek(self):
        if self.size == 0:
            raise Exception("size is 0")
        return self.items[0]

    # Removing min element and make last element root. Heapify down
    def poll(self):
        if self.size == 0:
            raise Exception("size is 0")
        item = self.items[0]
        self.items[0] = self.items[self.size - 1]
        self.size -= 1
        self.heapify_down()
        return item

    def add(self, item):
        self.ensure_extra_capacity()
        self.items[self.size] = item
        self.size += 1
        self.heapify_up()

    # Swap child element with parent (move stuff up)
    def heapify_up(self):
        index = self.size - 1
        while self.has_parent(index) and self.parent(index) > self.items[index]:
            self.swap(self.get_parent_index(index), index)
            index = self.get_parent_index(index)

    # Swap parent element with child (move stuff down)
    def heapify_down(self):
        index = 0

        # Only check Left, if no left, then certainly no right
        while self.has_left_child(index):
            smaller_child_index = self.get_left_child_index(index)
            if self.has_right_child(index) and self.right_child(index) < self.left_child(index):
                smaller_child_index = self.get_right_child_index(index)

            if self.items[index] < self.items[smaller_child_index]:
                break
            else:
                self.swap(index, smaller_child_index)
            index = smaller_child_index



