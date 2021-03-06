from  util.tree import TreeNode,deserialize
class Solution(object):
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

test=[
{"input":deserialize( [3,9,20,None,None,15,7]),"output":[
  [3],
  [9,20],
  [15,7]
]},
]
for t in test:
    r=s.levelOrder(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.levelOrder(t['input'])