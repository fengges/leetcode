from  util.tree import TreeNode,deserialize
class Solution:
    def maxLevelSum(self, root):
        levels=self.levelOrder(root)
        tmp=[[i,sum(v)] for i,v in enumerate(levels)]
        t=max(tmp,key=lambda x:x[1])
        return t[0]+1
    def levelOrder(self, root):
        r=[]
        if root:
            list=[root]
            next=0
            start=0
            level=[]
            while len(list)>start:
                tmp=list[start]
                if tmp.left:
                    list.append(tmp.left)
                if tmp.right:
                    list.append(tmp.right)
                level.append(tmp.val)
                if next==start:
                    r.append(level)
                    next=len(list)-1
                    level=[]
                start+=1
        return r

s=Solution()
null=None
test=[
{"input":deserialize( [1,7,0,7,-8,null,null]),"output":2},
]
for t in test:
    r=s.maxLevelSum(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
