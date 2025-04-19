def delete(self, key):
    if not self.head:
        return
    prev = self.head
    curr = self.head.next

    # Special case: only one node
    if self.head.key == key and self.head.next == self.head:
        self.head = None
        return

    while curr != self.head:
        if curr.key == key:
            prev.next = curr.next
            return
        prev = curr
        curr = curr.next

    # Check head after loop
    if self.head.key == key:
        prev.next = self.head.next
        self.head = self.head.next
