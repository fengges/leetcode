# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        t=ListNode(0)
        temp=None
        tail=t
        next=t
        while head:
            if head.val==temp:
                tail=next
            else:
                next=tail
                tail.next=head
                tail=head
                temp=head.val
            head=head.next

        tail.next=None
        return t.next

a1=ListNode(1)
a2=ListNode(2)
a3=ListNode(3)
a1.next=a2
a2.next=a3
b1=ListNode(3)
b2=ListNode(4)
b3=ListNode(4)
b4=ListNode(5)
a3.next=b1
b1.next=b2
b2.next=b3
b3.next=b4
s=Solution()
r=s.deleteDuplicates(a1)
print(r)
