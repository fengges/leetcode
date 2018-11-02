from util.link import ListNode,toLinkNode
class Solution:
    def middleNode(self, head):
        fast,slow=head,head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        return slow
