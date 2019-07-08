from util.tree import *
class Solution:

    def rob(self, root):
        if root is None:
            return 0
        left = 0
        right = 0
        leftSon = 0
        rightSon = 0
        if root.left:
            left = self.rob(root.left)
            if (root.left.left):
                leftSon = self.rob(root.left.left)
            if (root.left.right):
                leftSon += self.rob(root.left.right)
        if root.right:
            right = self.rob(root.right)
            if root.right.left:
                rightSon = self.rob(root.right.left)
            if root.right.right:
                rightSon += self.rob(root.right.right)
        return max(root.val + leftSon + rightSon, left + right)
    def rob2(self, root):
        if root is None:
            return 0
        return self.minCameraCover(root)
    def minCameraCover(self, root):
        a = self.find(root.left, True) + self.find(root.right, True)
        b = self.find(root.left, False) + self.find(root.right, False)
        t = max(a , b+root.val)
        if t == 0:
            return root.val
        else:
            return t
    # True 代表不偷
    def find(self, root, father):
        if not root:
            return 0
        if father:
            a = self.find(root.left, True) + self.find(root.right, True)
            b = self.find(root.left, False) + self.find(root.right, False)
            return max(a, b+ root.val)
        else:
            a = self.find(root.left, True) + self.find(root.right, True)
            return a

s=Solution()
null=None
test=[
{"input":deserialize([3,2,3,null,3,null,1]),"output": 7},

]
for t in test:
    r=s.minCameraCover(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))