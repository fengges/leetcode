from util.tree import *
class Solution:
    def maxAncestorDiff(self, root):
        self.r=0
        if root:
            path=[root.val]
            self.find(root.left,path)
            self.find(root.right,path)
            return self.r
        else:
            return 0
    def find(self,root,path):
        if root is None:
            num=max(path)-min(path)
            self.r=max(self.r,num)
            return
        path.append(root.val)
        self.find(root.left,path)
        self.find(root.right,path)
        path.pop()
null=None
s=Solution()
test=[
{"input": deserialize([8,3,10,1,6,null,14,null,null,4,7,13]), "output":7},
]

for t in test:
    r=s.maxAncestorDiff(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))

