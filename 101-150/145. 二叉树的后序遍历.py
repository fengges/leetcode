from  util.tree import TreeNode,deserialize
class Solution:
    def postorderTraversal(self, root):
        self.r = []
        self.find(root)
        return self.r

    def find(self, root):
        if root:
            self.find(root.left)
            self.find(root.right)
            self.r.append(root.val)
