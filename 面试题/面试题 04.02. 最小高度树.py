from util.tree import TreeNode
class Solution:
    def sortedArrayToBST(self, nums) :
        if not nums:
            return None
        mid = nums[len(nums)//2]
        idx = len(nums)//2
        root = TreeNode(mid)
        root.left = self.sortedArrayToBST(nums[:idx])
        root.right = self.sortedArrayToBST(nums[idx+1:])
        return root

