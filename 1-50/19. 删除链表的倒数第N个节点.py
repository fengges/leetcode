

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        s1=head
        s2=head
        for i in range(n):
            s1=s1.next
        if s1 is None:
            return head.next
        while s1.next  is not None:
            s1 = s1.next
            s2 = s2.next
        s2.next=s2.next.next
        return head

a1=ListNode(1)
a2=ListNode(2)
a3=ListNode(3)
# a1.next=a2
a2.next=a3
b1=ListNode(4)
b2=ListNode(5)
a3.next=b1
b1.next=b2
s=Solution()
r=s.removeNthFromEnd(a1,1)
print(r)




