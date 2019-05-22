from util.tree import *
class Solution:
    def rob(self, root):
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