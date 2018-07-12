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
        while head:
            if head.val==temp:
                pass
            else:
                tail.next=head
                tail=head
                temp=head.val
            head=head.next
        tail.next=None
        return t.next