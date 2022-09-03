# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        h=ListNode(0)
        t=h
        while l1 and l2:
            # print(l1.val,l2.val)
            if l1.val<=l2.val:
                t.next=l1
                l1=l1.next

            else:

                t.next=l2
                l2=l2.next
            t=t.next
        t.next= l1 if l1 else l2
        return h.next
