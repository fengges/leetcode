class Solution:
    def reverseList(self, head):
        t=ListNode(0)
        while head:
            tmp=head.next
            head.next=t.next
            t.next=head
            head=tmp
        return t.next