class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def findFrequentTreeSum(self, root):
        self.dic={}
        self.count(root)
        max=0
        for k in self.dic:
            if self.dic[k]>max:
                max=self.dic[k]
        r=[]
        for k in self.dic:
            if self.dic[k]==max:
                r.append(k)
        return r
    def count(self,root):
        if root is None:
            return 0
        sum=root.val+ self.count(root.left)+ self.count(root.right)
        if sum not in self.dic:
            self.dic[sum]=1
        else:
            self.dic[sum] += 1
        return sum


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
{"input":toTreeNode([5,2,-3]),"output": [2, -3, 4]},
{"input":toTreeNode([5,2,-5]),"output": [2]},
]
for t in test:
    r=s.findFrequentTreeSum(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.findFrequentTreeSum(t['input'])

