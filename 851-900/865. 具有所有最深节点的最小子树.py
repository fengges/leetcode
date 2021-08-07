from util.tree import TreeNode
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        ans=None
        maxl=-1
        def func(level,none):
            pass