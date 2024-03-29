# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        node=TreeNode(root.vak)
        node.left=self.mirrorTree(root.right)
        node.right=self.mirrorTree(root.left)
        return node