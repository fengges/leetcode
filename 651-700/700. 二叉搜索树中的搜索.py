from  util.tree import TreeNode,deserialize
class Solution:
    def searchBST(self, root, val):
        while root is not None and root.val!=val:
            if root.val<val:
                root=root.right
            else:
                root=root.left
        return root