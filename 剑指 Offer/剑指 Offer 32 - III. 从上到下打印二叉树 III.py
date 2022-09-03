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
        r[1::2]=[a[::-1] for a in r[1::2]]
        return r