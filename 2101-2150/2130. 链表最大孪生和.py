# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        ans=[]
        while head:
            ans.append(head.val)
            head=head.next
        val=float('-inf')
        size=len(ans)//2
        for i in range(size):
            val=max(val,ans[i]+ans[2*size-1-i])
        return val