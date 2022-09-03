class Solution:
    def numColor(self, root: TreeNode) -> int:
        ans=set()
        def fun(r):
            if r:
                ans.add(r.val)
                fun(r.right)
                fun(r.left)
        fun(root)
        return len(ans)