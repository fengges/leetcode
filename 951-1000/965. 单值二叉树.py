class Solution:
    def isUnivalTree(self, root):
        if root is None:
            return True
        return self.find(root,root.val)
    def find(self,root,val):
        if root is None:
            return True
        if root.val!=val:
            return False
        return self.find(root.left,val) and self.find(root.right,val)