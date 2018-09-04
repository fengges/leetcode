from  util.tree import TreeNode,deserialize
class Solution:
    def hasPathSum(self, root, sum):
        if root is None:
            return False
        return self.count(root,sum,0)

    def count(self,root,sum,now):
        if root.left is None and root.right is None:
            if  sum==now+root.val:
                return True
            else:
                return False
        elif root.right and root.left:
            return self.count(root.left,sum,now+root.val) or self.count(root.right,sum,now+root.val)
        elif root.right:
            return self.count(root.right, sum, now + root.val)
        else:
            return self.count(root.left, sum, now + root.val)



s=Solution()

test=[
{"input":[deserialize([1,2]),1],"output":False},
]
for t in test:
    r=s.hasPathSum(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))