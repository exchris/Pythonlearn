class DListNode:
    def __init__(self, val):
        self.val = val
        self.prev = self.next = Null

    def reverse(self, head):
        curr = None
        while head:
            curr = head
            head = curr.next
            curr.next = curr.prev
            curr.prev = head
        return curr
