class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root):
        list=[]
        result=[]
        temp=root
        while len(list)>0 or temp:
            while temp:
                list.append(temp)
                temp=temp.left
            if len(list)>0:
                temp=list[-1]
                result.append(temp.val)
                temp=temp.right
                del list[-1]
        return result
def toTreeNode2(nums):
    tree=[TreeNode(n) for n in nums]
    for i in range(len(nums)):
        if tree is None:
            continue
        if 2*i+1<len(nums) and tree[2*i+1].val:
            tree[i].left=tree[2*i+1]
        if 2 * i + 2 < len(nums) and tree[2 * i + 2].val:
            tree[i].right = tree[2 * i + 2]
    return tree[0]
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
{"input":toTreeNode([1,None,2,3]),"output":2},



]
for t in test:
    r=s.inorderTraversal(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.inorderTraversal(t['input'])




