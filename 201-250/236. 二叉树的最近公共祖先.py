from  util.tree import TreeNode,deserialize
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        left,right=[],[]
        self.find(root,p, left)
        self.find(root,q,right)
        r=root
        for i in range(min(len(left),len(right))):
            if left[i]==right[i]:
                r=left[i]
        return r
    def find(self,root,p,parent):
        parent.append(root)
        if root is None:
            return False
        if root.val==p.val:
            return True
        if self.find(root.left,p,parent):
            return True
        else:
            del parent[-1]
        if self.find(root.right,p,parent):
            return True
        else:
            del parent[-1]

s=Solution()

test=[
{"input":[deserialize([3,5,1,6,2,0,8,None,None,7,4]),TreeNode(5),TreeNode(4)],"output": 6},

]
for t in test:
    r=s.lowestCommonAncestor(t['input'][0],t['input'][1],t['input'][2])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
