class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head, val):
        t=ListNode(0)
        t.next=head
        head=t
        while t.next:
            if t.next.val==val:
                t.next=t.next.next
            else:
                t=t.next
        return head.next
