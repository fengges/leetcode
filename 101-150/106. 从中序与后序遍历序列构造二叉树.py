from  util.tree import TreeNode,deserialize
class Solution:
    def buildTree(self,  inorder, postorder):
        if len(postorder)==0:
            return None
        else:
            root=TreeNode(postorder[-1])
            index=inorder.index(postorder[-1])
            left=index
            root.left=self.buildTree(inorder[0:index],postorder[:left])
            root.right= self.buildTree(inorder[index+ 1:],postorder[left:-1])
            return root

s=Solution()
test=[
{"input":[[1,2,3,4],[3,4,2,1]], "output":[1,3,3,1]},
{"input":[[9,3,15,20,7],[9,15,7,20,3]], "output":[1,3,3,1]},
]

for t in test:
    r=s.buildTree(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
