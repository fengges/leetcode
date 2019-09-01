class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def insertIntoMaxTree(self, root, val):
        if root is None:
            return TreeNode(val)
        if val>root.val:
            t=TreeNode(val)
            t.left=root
            return t
        else:
            root.right=self.insertIntoMaxTree(root.right,val)
            return root
