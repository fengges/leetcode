class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def constructFromPrePost(self, pre, post):

            N=len(pre)
            if N==0:
                return None
            root=TreeNode(pre[0])
            L=0
            for i in range(N-1):
                if pre[1]==post[i]:
                    L=i+1
                    break
            root.left=self.constructFromPrePost(pre[1:L+1],post[:L])
            root.right=self.constructFromPrePost(pre[L+1:],post[L:-1])
            return root

s=Solution()

test=[
{"input":[[1,3,2,4],[3,4,2,1]],"output":[1,2,3,4,5,6,7]},
{"input":[[1,2,4,5,3,6,7], [4,5,2,6,7,3,1]],"output":[1,2,3,4,5,6,7]},

]

for t in test:
    r=s.constructFromPrePost(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))