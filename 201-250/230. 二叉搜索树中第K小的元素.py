class Solution:
    def kthSmallest(self, root, k):
        if root is None:
            return 0
        num=self.count(root.left)
        if num+1==k:
            return root.val
        if num+1<k:
            return self.kthSmallest(root.right,k-num-1)
        return self.kthSmallest(root.left,k)
    def count(self,root):
        if root is None:
            return 0
        return 1+self.count(root.left)+self.count(root.right)