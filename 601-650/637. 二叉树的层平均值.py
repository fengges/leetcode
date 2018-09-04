from  util.tree import TreeNode,deserialize
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

s=Solution()

test=[
{"input":deserialize( [3,9,20,15,7]),"output":[3.0,14.5,11.0]},
]
for t in test:
    r=s.averageOfLevels(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.averageOfLevels(t['input'])