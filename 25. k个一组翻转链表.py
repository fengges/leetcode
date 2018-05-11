class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        h=ListNode(0)
        h.next=head
        t=h
        while t.next is not None:
            last=t.next
            start1=last
            start2=last.next
            last.next = None
            i=1
            while i<k and start2 is not None:
                t.next=start2
                start2=start2.next
                t.next.next=start1
                start1=t.next
                i+=1
            if k!=i:
                last = t.next
                start1 = last
                start2 = last.next
                last.next=None
                while  start2 is not None:
                    t.next = start2
                    start2 = start2.next
                    t.next.next = start1
                    start1 = t.next
                t=last
            else:
                last.next=start2
                t=last

        return h.next

a0=ListNode(1)
a1=ListNode(2)
a2=ListNode(3)
a3=ListNode(4)
a4=ListNode(5)
a0.next=a1
a1.next=a2
a2.next=a3
a3.next=a4


s=Solution()
t=s.reverseKGroup(a0,2)
print(t)