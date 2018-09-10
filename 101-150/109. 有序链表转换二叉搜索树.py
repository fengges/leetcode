from  util.tree import TreeNode,deserialize

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def sortedListToBST(self, head):
        list=[]
        while head:
            list.append(head.val)
            head=head.next
        return self.sortedArrayToBST(list)
    def sortedArrayToBST(self, nums):
        if len(nums)==0:
            return None
        elif len(nums)==1:
            return TreeNode(nums[0])
        else:
            index=int(len(nums)/2)
            root=TreeNode(nums[index])
            root.left=self.sortedArrayToBST(nums[0:index])
            root.right=self.sortedArrayToBST(nums[index+1:])
            return root