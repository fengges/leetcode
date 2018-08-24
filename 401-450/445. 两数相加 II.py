class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        num1=0
        while l1:
            num1=num1*10+l1.val
            l1=l1.next
        num2=0
        while l2:
            num2=num2*10+l2.val
            l2=l2.next

        t=str(num1+num2)
        head=ListNode(0)
        tail=head
        for s in t:
            tmp=ListNode(int(s))
            tail.next=tmp
            tail=tmp
        return head.next


