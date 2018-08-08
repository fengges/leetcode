# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumOfLeftLeaves(self, root):
        if root is None:
            return 0
        if root.left is None :
            return self.sumOfLeftLeaves(root.right)
        elif root.left.left is None and root.left.right is None:
            return root.left.val+self.sumOfLeftLeaves(root.right)
        else:
            return self.sumOfLeftLeaves(root.left)+self.sumOfLeftLeaves(root.right)


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
{"input":toTreeNode([0,2,4,1,None,3,-1,5,1,None,6,None,8]),"output":5},
{"input":toTreeNode([3,9,20,None,None,15,7]),"output":24},
]
for t in test:
    r=s.sumOfLeftLeaves(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.sumOfLeftLeaves(t['input'])