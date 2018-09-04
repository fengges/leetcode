from  util.tree import TreeNode,deserialize
class Solution:
    def invertTree(self, root):
        if root:
            tmp=root.left
            root.left=self.invertTree(root.right)
            root.right=self.invertTree(tmp)
        return root