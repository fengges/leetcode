
from util.tree import *
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        def levelOrderBottom(root):
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
            r.reverse()
            return r
        arr=levelOrderBottom(root)
        if len(arr)>0:
            return sum(arr[0])
        else:
            return 0

s=Solution()
null=None
test=[
{"input":deserialize( [1,2,3,4,5,null,6,7,null,null,null,null,8]),"output":15},
]
for t in test:
    r=s.deepestLeavesSum(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
