import collections


class Queue:
    def __init__(self):
        self._data = collections.deque()

    # Insert at tail
    def enqueue(self, x):
        self._data.append(x)

    # Remove at head
    def dequeue(self):
        return self._data.popleft()

    # Get head value
    def max(self):
        return max(self._data)


q = Queue()
q.enqueue(3)
print(q.max())