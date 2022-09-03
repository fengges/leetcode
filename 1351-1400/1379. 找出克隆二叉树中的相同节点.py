class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        # print(original.val,cloned.val,target.val)
        if cloned.val==target.val:
            return cloned
        ans=None
        if original.left:
            ans=self.getTargetCopy(original.left,cloned.left,target)
        if ans is None and original.right:
            return self.getTargetCopy(original.right,cloned.right,target)
        return ans