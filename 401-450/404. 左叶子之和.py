# Definition for a binary tree node.
from  util.tree import TreeNode,deserialize

class Solution:
    def sumOfLeftLeaves(self, root):
        if root is None:
            return 0
        if root.left is None :
            return self.sumOfLeftLeaves(root.right)
        elif root.left.left is None and root.left.right is None:
            return root.left.val+self.sumOfLeftLeaves(root.right)
        else:
            return self.sumOfLeftLeaves(root.left)+self.sumOfLeftLeaves(root.right)


s=Solution()

test=[
{"input":deserialize([0,2,4,1,None,3,-1,5,1,None,6,None,8]),"output":5},
{"input":deserialize([3,9,20,None,None,15,7]),"output":24},
]
for t in test:
    r=s.sumOfLeftLeaves(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.sumOfLeftLeaves(t['input'])