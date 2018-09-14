from  util.tree import TreeNode,deserialize
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if root is None:
            return None
        elif (root.val>=p.val and root.val<=q.val) or (root.val<=p.val and root.val>=q.val):
            return root
        elif root.val<p.val and root.val<q.val:
            return self.lowestCommonAncestor(root.right,p,q)
        else:
            return self.lowestCommonAncestor(root.left,p,q)