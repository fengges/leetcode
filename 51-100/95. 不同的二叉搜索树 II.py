from  util.tree import TreeNode,deserialize

class Solution:
    def generateTrees(self, n):
        return self.bulit(1,n)
    def bulit(self,s,e):
        re=[]
        for i in range(s,e+1):
            left=self.bulit(s,i-1)
            right=self.bulit(i+1,e)
            if len(left) == 0:
                left.append(None)
            if len(right)==0:
                right.append(None)
            for l in left:
                for r in right:
                    root=TreeNode(i)
                    root.left=l
                    root.right=r
                    re.append(root)
        return re
s=Solution()
test=[
{"input":3,"output":2},



]
for t in test:
    r=s.generateTrees(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.generateTrees(t['input'])