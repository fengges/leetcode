# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        h=ListNode(0)
        t=h
        while l1 is not None and l2 is not None:
            if l1.val<=l2.val:
                t.next=l1
                t=l1
                l1=l1.next
            else:
                t.next=l2
                t=l2
                l2=l2.next
        if l1 is None:
            temp=l2
        else:
            temp=l1
        while temp is not None:
            t.next=temp
            t=temp
            temp=temp.next
        return h.next

a1=ListNode(1)
a2=ListNode(2)
a3=ListNode(4)
a1.next=a2
a2.next=a3
b1=ListNode(1)
b2=ListNode(3)
b3=ListNode(4)
b1.next=b2
b2.next=b3
s=Solution()
t=s.mergeTwoLists(a1,b1)
print(t)