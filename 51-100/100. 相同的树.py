# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        elif p is not None and q is not None and p.val==q.val:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        else:
            return False