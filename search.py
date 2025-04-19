def search(self, key):
    if not self.head:
        return None
    current = self.head
    while True:
        if current.key == key:
            return current
        current = current.next
        if current == self.head:
            break
    return None
