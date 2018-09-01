class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        t=ListNode(0)
        while head:
            tmp=head.next
            head.next=t.next
            t.next=head
            head=tmp
        return t.next
