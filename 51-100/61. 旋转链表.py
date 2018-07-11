# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head, k):
        if head is None:
            return
        t1=head
        t2=head
        lens=0
        for i in range(k):
            t1=t1.next
            lens+=1
            if t1 is None:
                t1=head
                k=k-int(k/lens)*lens
                for j in range(k):
                    t1 = t1.next
                break

        while t1.next:
            t1=t1.next
            t2=t2.next
        t1.next=head
        head=t2.next
        t2.next=None
        return head


a0=ListNode(1)
a1=ListNode(2)
a2=ListNode(3)
a3=ListNode(4)
a4=ListNode(5)
a0.next=a1
a1.next=a2
# a2.next=a3
a3.next=a4

s=Solution()
t=s.rotateRight(a0,4)
print(t)