from  util.tree import TreeNode,deserialize
class Solution:
    def preorderTraversal(self, root):
        self.r=[]
        self.find(root)
        return self.r
    def find(self,root):
        if root:
            self.r.append(root.val)
            self.find(root.left)
            self.find(root.right)
