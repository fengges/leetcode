from  util.tree import TreeNode,deserialize
class Solution:
    def maxPathSum(self, root):
        if root == None:
            return 0
        Max = -10000000
        r,Max=self.maxpath(root, Max)
        return Max

    def maxpath(self,root,Max):
        if root==None:
            return 0,Max
        l,Max = self.maxpath(root.left, Max)
        r,Max = self.maxpath(root.right, Max)
        Max=max(Max, max(0, l) + max(0, r) + root.val)
        return max(0,max(l,r))+root.val,Max

s=Solution()

test=[
{"input":deserialize([-10,9,20,None,None,15,7]),"output":42},
{"input":deserialize([1,2,3]),"output":6},
]
for t in test:
    r=s.maxPathSum(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))

