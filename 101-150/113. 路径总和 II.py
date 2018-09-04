from  util.tree import TreeNode,deserialize
import copy
class Solution:
    def pathSum(self, root, sum):
        self.result=[]
        if root:
            self.add(root,sum,[])
        return self.result
    def add(self,root,all,num):
        num.append(root.val)
        if sum(num)==all:
            if root.left is None and root.right is None:
                self.result.append(copy.deepcopy(num))
        if root.left:
            self.add(root.left,all,num)
        if root.right:
            self.add(root.right,all,num)
        del num[-1]
s=Solution()

test=[
{"input":[deserialize([-2,None,-3]),-5],"output":[[-2,-3]]},
]
for t in test:
    r=s.pathSum(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))