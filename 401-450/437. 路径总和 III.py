from  util.tree import TreeNode,deserialize
class Solution(object):
    def pathSum(self, root, sum):
        if root is None:
            return 0
        return self.add(root,sum)+self.pathSum(root.left,sum)+self.pathSum(root.right,sum)
    def add(self,root,sum):
        if root is None:
            return 0
        res=0
        if sum==root.val:
            res=1
        return res+self.add(root.left,sum-root.val)+self.add(root.right,sum-root.val)

s=Solution()
test=[
{"input":[deserialize([1,-2,-3,1,3,-2,None,-1]),-1],"output": 4},
{"input":[deserialize([10,5,-3,3,2,None,11,3,-2,None,1]),8],"output": 3},
]
for t in test:
    r=s.pathSum(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))