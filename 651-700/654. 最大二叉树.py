from  util.tree import TreeNode,deserialize
class Solution:
    def constructMaximumBinaryTree(self, nums):
        if len(nums)==0:
            return None
        index=nums.index(max(nums))
        root=TreeNode(nums[index])
        root.left=self.constructMaximumBinaryTree(nums[0:index])
        root.right = self.constructMaximumBinaryTree(nums[index+1:])
        return root

