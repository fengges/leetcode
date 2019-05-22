from util.tree import *
class Solution:
    def distributeCoins(self, root):
        self.sum = 0
        self.help(root)
        return self.sum

    def help(self,root):
        if root is None:
            return 0
        left = self.help(root.left)
        right = self.help(root.right)
        self.sum += abs(root.val - 1 + left + right)
        return root.val - 1 + left + right

s=Solution()
null=None
test=[
{"input":deserialize([5,0,0,0,null,null,0,null,null,null,null]),"output": 2},

]
for t in test:
    r=s.distributeCoins(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
