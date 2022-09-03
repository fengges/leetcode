# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        t=head
        t1,t2=head,head
        for i in range(k):
            t1=t1.next

        while t1:
            t1=t1.next
            t2=t2.next
        return t2