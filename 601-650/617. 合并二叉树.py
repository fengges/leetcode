from  util.tree import TreeNode,deserialize
class Solution:
    def mergeTrees(self, t1, t2):
        if t1 is None and t2 is None:
            return None
        elif t1 is None:
            return t2
        elif t2 is None:
            return t1
        else:
            root=TreeNode(t1.val+t2.val)
            root.left=self.mergeTrees(t1.left,t2.left)
            root.right=self.mergeTrees(t1.right,t2.right)
            return root