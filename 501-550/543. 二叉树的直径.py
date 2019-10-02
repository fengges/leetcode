from util.tree import *
__d
class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# deserialize
class Solution:
    def diameterOfBinaryTree(self, root):
        _,r=self.find(root)
        return r

    def find(self,root):
        if root:
            l1,l2=self.find(root.left)
            r1,r2 =self.find(root.right)
            val=l1+r1
            return max(l1,r1)+1,max(l2,r2,val)
        else:
            return 0,0
null=None
s = Solution()
test = [
{"input":deserialize([1,2,3,4,5]), "output":3},
]

for t in test:
    r = s.diameterOfBinaryTree(t['input'])
    if r != t['output']:
        print("error:" + str(t) + " out:" + str(r))

