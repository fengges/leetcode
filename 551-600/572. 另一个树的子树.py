# Definition for a binary tree node.
from  util.tree import TreeNode,deserialize
class Solution(object):
    def isSubtree(self, s, t):
        if s is not None :
            if self.isSameTree(s,t):
                return True
            return self.isSubtree(s.left,t) or self.isSubtree(s.right,t)
        else:
            return False
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        elif p is not None and q is not None and p.val==q.val:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        else:
            return False