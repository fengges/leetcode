from  util.tree import TreeNode,deserialize
class Solution:
    def isSymmetric(self, root):
        if root is None:
            return True
        return self.isSymmetricLeftRight(root.left,root.right)
    def isSymmetricLeftRight(self, left,right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val!=right.val:
            return False
        return self.isSymmetricLeftRight(left.left, right.right) and self.isSymmetricLeftRight(left.right, right.left)


s=Solution()

test=[
{"input":deserialize([1,2,3,3,None,2,None]),"output":False},
{"input":deserialize([1,None,2,3]),"output":False},
{"input":deserialize([1,2,2,3,4,4,3]),"output":True},
{"input":deserialize([1,2,2,None,3,None,3]),"output":False},

]
for t in test:
    r=s.isSymmetric(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.isSymmetric(t['input'])