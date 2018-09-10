from util.link import ListNode,toLinkNode
class Solution:
    def splitListToParts(self, root, k):
        size=0
        h=root
        while h:
            h=h.next
            size+=1
        length=int(size/k)
        r=[length for i in range(k)]
        left=size-length*k
        for i in range(left):
            r[i]+=1
        head=ListNode(0)
        head.next=root
        re=[]
        for i in r:
            re.append(head.next)
            temp=head
            for j in range(i):
                head=head.next
            temp.next=None
        return re
s=Solution()

test=[
{"input":[toLinkNode([1,2,3]),5],"output":[[1],[2],[3],[],[]]},
{"input":[toLinkNode([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),3],"output":[[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]},
]


for t in test:
    r=s.splitListToParts(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))




