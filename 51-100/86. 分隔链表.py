class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head, x):
        t,h=ListNode(0),ListNode(0)
        t1,h1=t,h
        while head:
            if head.val<x:
                t.next=head
                t=head
            else:
                h.next=head
                h=head
            head=head.next
        h.next=None
        t.next=h1.next
        return t1.next


a1=ListNode(1)
a2=ListNode(4)
a3=ListNode(3)
a1.next=a2
a2.next=a3
b1=ListNode(2)
b2=ListNode(5)
b3=ListNode(2)
b4=ListNode(5)
a3.next=b1
b1.next=b2
b2.next=b3

s=Solution()
r=s.partition(a1,3)
print(r)
