from  util.tree import TreeNode,deserialize
class Solution:
    def deleteNode(self, root, key):
        if root is None:
            return None
        if root.val>key:
            root.left=self.deleteNode(root.left,key)
        elif root.val<key:
            root.right=self.deleteNode(root.right,key)
        else:
            if root.left is None:
                root=root.right
            elif root.right is None:
                root=root.left
            else:
                tmp=root.left
                while tmp.right:
                    tmp=tmp.right
                root.val=tmp.val
                root.left=self.deleteNode(root.left,tmp.val)
        return root