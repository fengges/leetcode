from util.tree import *
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def cmp(l,r):
            if not l and not r:
                return True
            elif l and r:
                return l.val==r.val and cmp(l.left,r.right) and cmp(l.right,r.left)
            else:
                return False
        return cmp(root.left,root.right) if root is not None else True

s=Solution()
null=None
test=[
    {"input":deserialize([]),"output":True},
    {"input":deserialize( [1,2,2,null,3,null,3]),"output":False},
    {"input":deserialize([1,2,2,3,4,4,3]),"output":True},


]
for t in test:
    r=s.isSymmetric(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))