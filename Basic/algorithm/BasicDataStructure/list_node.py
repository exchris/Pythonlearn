class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    # in python next is a reversed world
    def reverse(self, head):
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev


