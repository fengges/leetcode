class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        if len(preorder)==0:
            return None
        else:
            root=TreeNode(preorder[0])
            index=inorder.index(preorder[0])
            left=index
            root.left=self.buildTree(preorder[1:1+left],inorder[0:index])
            root.right= self.buildTree(preorder[1 + left:], inorder[index+ 1:])
            return root

s=Solution()
test=[
{"input":[[3,9,20,15,7],[9,3,15,20,7]], "output":[1,3,3,1]},
]

for t in test:
    r=s.buildTree(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
