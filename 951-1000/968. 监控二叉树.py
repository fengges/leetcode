from util.tree import *
class Solution:
    def minCameraCover2(self, root):
        a = self.find(root.left, True) + self.find(root.right, True)
        b = self.find(root.left, False) + self.find(root.right, False)
        t=min(a + 1, b)
        if t==0:
            return 1
        else:
            return t
    def find(self,root,father):
        if not root:
            return 0
        if father:
            a = self.find(root.left, True) + self.find(root.right, True)
            b=self.find(root.left,False)+self.find(root.right,False)
            return min(a+1,b)
        else:
            a = self.find(root.left, True) + self.find(root.right, True)
            return a+1

    def minCameraCover(self,root):
        self.ans=0
        if root is None:
            return 0
        if self.dfs(root) == 2:
            self.ans=+1
        return self.ans

    def dfs(self,node):
        if node is None:
            return 1
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        if (left == 2 or right == 2):
            self.ans+=1
            return 0
        elif (left == 0 or right == 0):
            return 1
        else:
            return 2
s=Solution()
null=None
test=[
{"input":deserialize([0,0,null,null,0,0,null,null,0,0]),"output": 2},
{"input":deserialize([0]),"output": 1},
{"input":deserialize([0,0,null,0,0]),"output": 1},
{"input":deserialize([0,0,null,0,null,0,null,null,0]),"output": 2},
]
for t in test:
    r=s.minCameraCover(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))