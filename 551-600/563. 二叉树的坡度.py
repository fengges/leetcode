class Solution:
    def findTilt(self, root):
        v1,v2=self.count(root)
        return v2
    def count(self,root):
        if root is None:
            return 0,0
        left1,left2=self.count(root.left)
        right1,right2=self.count(root.right)
        return left1+right1+root.val,abs(left1-right1)+left2+right2
