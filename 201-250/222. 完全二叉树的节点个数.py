from  util.tree import TreeNode,deserialize
class Solution:
    def countNodes(self, root):
        if root:
            n=self.isFullTree(root)
            if n==0:
                return self.countNodes(root.left)+self.countNodes(root.right)+1
            else:
                return n
        return 0
    def isFullTree(self,root):
        l,r=0,0
        nl,nr=root,root
        while nl:
            nl=nl.left
            l+=1
        while nr:
            nr = nr.right
            r += 1
        if l==r:
            return (1<<l)-1
        else:
            return 0

s=Solution()

test=[
{"input":deserialize([1,2,3,4,5,6]),"output": 6},

]
for t in test:
    r=s.countNodes(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))

