class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def canFinish(self, numCourses, prerequisites):
        head=[ListNode(i) for i in range(numCourses)]
        tail=[i for i in head]
        for i in  prerequisites:
            tmp=ListNode(i[1])
            tail[i[0]].next=tmp
            tail[i[0]]=tmp
        while True:
            index=self.find(head)
            if index<0:
                break
            self.delete(head,head[index].val)
            del head[index]
        return len(head)==0
    def delete(self,head,val):
        for i in head:
            tmp=i
            while tmp.next:
                if tmp.next.val==val:
                    tmp.next=tmp.next.next
                    continue
                tmp=tmp.next

    def find(self,head):
        if len(head)==0:
            return -1
        for i in range(len(head)):
            if head[i].next is None:
                return i
        return -1

s=Solution()
test=[
{"input": [3,[[1,0],[2,1]]], "output":True},
{"input": [2,[[1,0]]], "output":True},

]

for t in test:
    r=s.canFinish(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))

