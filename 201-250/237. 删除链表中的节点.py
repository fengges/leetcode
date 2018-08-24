class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """


def toLinkNode(nums):
    head=ListNode(0)
    temp=head
    for n in nums:
        t = ListNode(n)
        temp.next=t
        temp=t
    return head.next
s=Solution()

test=[
{"input":[toLinkNode([3,5]),1,1],"output":2},
{"input":[toLinkNode([3,5]),1,2],"output":2},
{"input":[toLinkNode([1,2,3,4,5]),2,4],"output":2},

{"input":[toLinkNode([5]),1,1],"output":2},


]
for t in test:
    r=s.deleteNode(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))