# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        h=ListNode(float('inf'))
        h.next=head
        t=h
        while t.next:
            if t.next.val==val:
                t.next=t.next.next
                break
            else:
                t=t.next
        return h.next