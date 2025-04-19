class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

class CircularLinkedListDict:
    def __init__(self):
        self.head = None

    def insert(self, key):
        new_node = Node(key)
        if not self.head:
            new_node.next = new_node  # points to itself
            self.head = new_node
        else:
            new_node.next = self.head.next
            self.head.next = new_node
