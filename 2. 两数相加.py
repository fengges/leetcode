
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def addTwoNumbers(self, l1, l2):
        t=ListNode(0)
        l=t
        flag=0
        while l1 is not None and l2 is not None:
            sum=l1.val+l2.val+flag
            if sum>=10:
                sum-=10
                flag=1
            else:
                flag=0
            a=ListNode(sum)
            l1=l1.next
            l2=l2.next
            l.next=a
            l=a
        if l1 is None:
            l1=l2
        while l1 is not None:
            sum=l1.val+flag
            if sum>=10:
                sum-=10
                flag=1
            else:
                flag=0
            a=ListNode(sum)
            l1=l1.next
            l.next=a
            l=a
        if flag>0:
            a=ListNode(flag)
            l.next=a
        return t.next



# (2 -> 4 -> 3) + (5 -> 6 -> 4)
# a1=ListNode(2)
# a2=ListNode(4)
# a3=ListNode(3)
# a1.next=a2
# a2.next=a3
# b1=ListNode(5)
# b2=ListNode(6)
# b3=ListNode(4)
# b1.next=b2
# b2.next=b3
a1=ListNode(1)
a2=ListNode(8)
a1.next=a2
b1=ListNode(0)
s=Solution()
t=s.addTwoNumbers(a1,b1)
print(t)
