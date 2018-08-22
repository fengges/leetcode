class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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
{"input":[toTreeNode([1,2]),1],"output":False},
]
for t in test:
    r=s.hasPathSum(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))