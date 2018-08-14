class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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

def toTreeNode(nums):
    tree=[TreeNode(n) for n in nums]
    f=0
    i=1
    while i<len(tree):
        if tree[f].val is None:
            f+=1
            continue
        if tree[i].val:
            tree[f].left=tree[i]
        else:
            tree[f].left = None
        i += 1
        if i==len(tree):
            break
        if tree[i].val:
            tree[f].right=tree[i]
        else:
            tree[f].right = None
        i += 1
        f+=1
    return tree[0]
s=Solution()

test=[
{"input":toTreeNode([1,2,3,3,None,2,None]),"output":False},
{"input":toTreeNode([1,None,2,3]),"output":False},
{"input":toTreeNode([1,2,2,3,4,4,3]),"output":True},
{"input":toTreeNode([1,2,2,None,3,None,3]),"output":False},

]
for t in test:
    r=s.isSymmetric(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.isSymmetric(t['input'])