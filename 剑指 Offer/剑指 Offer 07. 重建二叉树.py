class Solution:
    def buildTree(self, preorder, inorder):
        if len(preorder)==0:
            return None
        else:
            root=TreeNode(preorder[0])
            index=inorder.index(preorder[0])
            left=index
            root.left=self.buildTree(preorder[1:1+left],inorder[0:index])
            root.right= self.buildTree(preorder[1 + left:], inorder[index+ 1:])
            return root