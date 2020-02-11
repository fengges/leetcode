from util.tree import *
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        ans=0
        if root is None:
            return ans
        if root.val%2==0:
            if root.left:
                if root.left.left:
                    ans+=root.left.left.val
                if root.left.right:
                    ans+=root.left.right.val
            if root.right:
                if root.right.left:
                    ans += root.right.left.val
                if root.right.right:
                    ans += root.right.right.val
        ans+=self.sumEvenGrandparent(root.left)+self.sumEvenGrandparent(root.right)
        return ans

s=Solution()
null=None
test=[
{"input":deserialize([6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]),"output":18},
]
for t in test:
    r=s.sumEvenGrandparent(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
