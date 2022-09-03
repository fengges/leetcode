
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def toLinkNode(nums,C=False):
    head=ListNode(0)
    temp=head
    for n in nums:
        t = ListNode(n)
        temp.next=t
        temp=t
    if C:
        temp.next=head.next
    return head.next

# nums=[1,2]
# for n,v in enumerate(nums):
#     print(n)