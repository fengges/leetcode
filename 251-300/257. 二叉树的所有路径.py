class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import copy
class Solution:
    def binaryTreePaths(self, root):
        self.result=[]
        if root:
            self.find(root,[])
            self.result=[ "->".join(r) for r in self.result]
        return self.result
    def find(self,root,num):
        num.append(str(root.val))
        if root.left is None and root.right is None:
            self.result.append(copy.deepcopy(num))
        elif root.left is None:
            self.find(root.right,num)
        elif root.right is None:
            self.find(root.left,num)
        else:
            self.find(root.left, num)
            self.find(root.right, num)
        del num[-1]

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
{"input":toTreeNode([1,2,3,None,5]),"output": [2, -3, 4]},

]
for t in test:
    r=s.binaryTreePaths(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
