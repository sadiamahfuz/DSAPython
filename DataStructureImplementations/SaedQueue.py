class Node:
    def __init__(self, x):
        self.x = x
        self.next = None


class SaedQueue:
    """
    Implementation of Queue Using LinkedList
    FIFO
    Add to the tail
    Remove from Head
    Add/Remove -> O(1)
    """
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def add(self, val):
        prev_node = self.tail
        self.tail = Node(val)

        if self.is_empty():
            self.head = self.tail
            self.tail.next = None
        else:
            prev_node.next = self.tail

    def remove(self):
        if self.head is None:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next

    def print(self):
        temp = self.head
        while temp:
            print(temp.x, end=' -> ')
            temp = temp.next

        print("None")


queue = SaedQueue()
queue.add(2)
queue.add(4)
queue.add(5)
queue.add(3)

queue.print()

queue.remove()
queue.remove()
queue.print()

queue.remove()
queue.remove()
queue.print()
