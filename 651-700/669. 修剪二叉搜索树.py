class Solution:
    def trimBST(self, root, L, R):
        if root is None:
            return root
        else:
            if root.val>=L and root.val<=R:
                root.left=self.trimBST(root.left,L,R)
                root.right=self.trimBST(root.right, L, R)
            elif root.val<L:
                root=self.trimBST(root.right)
            else:
                root = self.trimBST(root.left)
        return root
        pass
