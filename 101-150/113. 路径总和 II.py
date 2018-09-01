class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import copy
class Solution:
    def pathSum(self, root, sum):
        self.result=[]
        if root:
            self.add(root,sum,[])
        return self.result
    def add(self,root,all,num):
        num.append(root.val)
        if sum(num)==all:
            if root.left is None and root.right is None:
                self.result.append(copy.deepcopy(num))
        if root.left:
            self.add(root.left,all,num)
        if root.right:
            self.add(root.right,all,num)
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
{"input":[toTreeNode([-2,None,-3]),-5],"output":[[-2,-3]]},
]
for t in test:
    r=s.pathSum(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))