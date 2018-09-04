from  util.tree import TreeNode,deserialize
class Solution:
    def isBalanced(self, root):
        h,t=self.count(root)
        return t

    def count(self,root):
        if root:
            left,isleft=self.count(root.left)
            right,isright = self.count(root.right)
            if isleft and isright and abs(left-right)<=1:
                return max(left,right)+1,True
            else:
                return max(left,right)+1,False
        return 0,True

s=Solution()

test=[
{"input":deserialize( [1,2,2,3,3,None,None,4,4]),"output":False},
]
for t in test:
    r=s.isBalanced(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.isBalanced(t['input'])