
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def averageOfLevels(self, root):
        r = []
        if root:
            list = [root]
            next = 0
            start = 0
            level = []
            while len(list) > start:
                tmp = list[start]
                if tmp.left:
                    list.append(tmp.left)
                if tmp.right:
                    list.append(tmp.right)
                level.append(tmp.val)
                if next == start:
                    r.append(level)
                    next = len(list) - 1
                    level = []
                start += 1
        return [ sum(t)/len(t) for t in r]

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
{"input":deserialize( [3,9,20,15,7]),"output":[3.0,14.5,11.0]},
]
for t in test:
    r=s.averageOfLevels(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.averageOfLevels(t['input'])