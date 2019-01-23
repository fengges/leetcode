class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def allPossibleFBT(self, N):
        if N%2==0:
            return []
        else:
            result = []
            if N==1:
                return [TreeNode(0)]
            for i in range(1,N-1,2):
                left=self.allPossibleFBT(i)
                right=self.allPossibleFBT(N-1-i)
                for l in left:
                    for r in right:
                        node=TreeNode(0)
                        node.left=l
                        node.right=r
                        result.append(node)
            return result
null=None
s = Solution()
test = [
    {"input": 7, "output": [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]},

]

for t in test:
    r = s.allPossibleFBT(t['input'])
    if r != t['output']:
        print("error:" + str(t) + " out:" + str(r))