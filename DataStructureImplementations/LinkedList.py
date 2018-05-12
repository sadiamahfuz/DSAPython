class Node:
    def __init__(self, x):
        self.x = x
        self.next = None


class MyLinkedList:
    """
    Linked List where elements are added to the end of the list
    add is O(1)
    remove is O(n)
    reverse is O(n)
    """
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, val):
        if self.head is None:
            self.head = Node(val)
            self.head.next = None
            self.tail = self.head
        else:
            temp = self.tail
            self.tail = Node(val)
            temp.next = self.tail

    def remove(self, val):
        if self.head is None:
            return

        if self.head.x is val:
            self.head = self.head.next
            return

        prev = self.head
        curr = self.head.next
        while curr is not None:
            if curr.x is val:
                if self.tail is curr:
                    self.tail = prev
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next

    def reverse(self):
        curr_node = self.head
        prev_node = None

        while curr_node:
            temp_next = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = temp_next

        temp_node = self.head
        self.head = prev_node
        self.tail = temp_node

    def print(self):
        temp = self.head
        while temp:
            print(temp.x, end=' -> ')
            temp = temp.next

        print("None")


myList = MyLinkedList()
myList.add(1)
myList.add(3)
myList.add(4)
myList.add(6)
myList.add(7)
myList.add(9)


myList.reverse()
myList.print()
