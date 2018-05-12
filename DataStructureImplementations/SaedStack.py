class Node:
    def __init__(self, x):
        self.x = x
        self.next = None


class SaedStack:
    """
    Implementation of Stack Using LinkedList
    FILO
    Add and Remove from Head O(1)
    """
    def __init__(self):
        self.head = None

    def push(self,  x):
        if self.head is None:
            self.head = Node(x)
        else:
            prev_node = self.head
            self.head = Node(x)
            self.head.next = prev_node

    def pop(self):
        self.head = self.head.next

    def print(self):
        temp = self.head
        while temp is not None:
            print(temp.x, end=' -> ')
            temp = temp.next
        print("None")


stack = SaedStack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

stack.print()
stack.pop()
stack.print()
