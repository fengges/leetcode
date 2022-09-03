# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        ans=[]
        def fun(node):
            if node:
                fun(node.next)
                ans.append(node.val)
        fun(head)
        return ans