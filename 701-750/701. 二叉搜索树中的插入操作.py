from  util.tree import TreeNode,deserialize
class Solution:
    def insertIntoBST(self, root, val):
        t=root
        while root is not None and root.val!=val:
            if root.val<val:
                if root.right is None:
                    root.right=TreeNode(val)
                    break
                root=root.right
            else:
                if root.left is None:
                    root.left=TreeNode(val)
                    break
                root=root.left
        return t
