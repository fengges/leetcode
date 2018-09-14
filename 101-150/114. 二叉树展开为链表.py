class Solution:
    def flatten(self, root):
        if root is None:
            return
        if root.left:
            self.flatten(root.left)
        if root.right:
            self.flatten(root.right)
        right=root.right
        root.right=root.left
        root.left=None
        while root.right:
            root=root.right
        root.right=right