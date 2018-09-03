class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumNumbers(self, root):
        self.result=[]
        if root:
            self.find(root,0)
        return sum(self.result)
    def find(self,root,num):
        num=num*10+root.val
        if root.left is None and root.right is None:
            self.result.append(num)
        elif root.left is None:
            self.find(root.right,num)
        elif root.right is None:
            self.find(root.left,num)
        else:
            self.find(root.left, num)
            self.find(root.right, num)

def deserialize(nums):
    if len(nums)==0:
        return None
    tree = [TreeNode(n) for n in nums]
    f = 0
    i = 1
    while i < len(tree):
        if tree[f].val is None:
            f += 1
            continue
        if tree[i].val is not None:
            tree[f].left = tree[i]
        else:
            tree[f].left = None
        i += 1
        if i == len(tree):
            break
        if tree[i].val is not None:
            tree[f].right = tree[i]
        else:
            tree[f].right = None
        i += 1
        f += 1
    return tree[0]
s=Solution()

test=[
{"input":deserialize([1,2,3,None,5,None,None]),"output":25},
]
for t in test:
    r=s.sumNumbers(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.sumNumbers(t['input'])