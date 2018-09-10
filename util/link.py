
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def toLinkNode(nums):
    head=ListNode(0)
    temp=head
    for n in nums:
        t = ListNode(n)
        temp.next=t
        temp=t
    return head.next