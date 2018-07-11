class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        h=ListNode(0)
        h.next=head
        t=h
        while t is not None and t.next is not None and t.next.next is not None:
             temp=t.next
             t.next=t.next.next
             temp.next=t.next.next
             t.next.next=temp
             t=temp
        return h.next
a0=ListNode(1)
a1=ListNode(2)
a2=ListNode(3)
a3=ListNode(4)
a0.next=a1
a1.next=a2
a2.next=a3


s=Solution()
t=s.swapPairs(a0)
print(t)