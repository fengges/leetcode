class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def constructMaximumBinaryTree(self, nums):
        if len(nums)==0:
            return None
        index=nums.index(max(nums))
        root=TreeNode(nums[index])
        root.left=self.constructMaximumBinaryTree(nums[0:index])
        root.right = self.constructMaximumBinaryTree(nums[index+1:])
        return root

