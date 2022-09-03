class Solution:
    def __init__(self):
        self.pre=None
    def treeToDoublyList(self , pRootOfTree ):
        def order(root):
            if not root: return
            order(root.left)
            root.left=self.pre
            if self.pre:
                self.pre.right=root
            self.pre=root
            order(root.right)
        if not pRootOfTree: return
        p=pRootOfTree
        while p.left:
            p=p.left
        order(pRootOfTree)
        return p
from util.tree import deserialize
s=Solution()
test=[

    {"input":  deserialize([10,6,14,4,8,12,16]),"output":[3,3,5,5,6,7]},

]

for t in test:
    r=s.treeToDoublyList(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))