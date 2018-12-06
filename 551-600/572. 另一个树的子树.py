# Definition for a binary tree node.
from  util.tree import TreeNode,deserialize
class Solution(object):
    def isSubtree(self, s, t):
        if s is not None :
            return self.isSameTree(s,t) or self.isSubtree(s.left,t) or self.isSubtree(s.right,t)
        else:
            return False
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        elif p is not None and q is not None and p.val==q.val:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        else:
            return False
null=None
s=Solution()
test=[
{"input":[deserialize([1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,2]),deserialize([1,null,1,null,1,null,1,null,1,null,1,2])], "output":2},

]
for t in test:
    r=s.isSubtree(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))