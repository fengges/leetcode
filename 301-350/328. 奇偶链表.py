from util.link import ListNode,toLinkNode
class Solution:
    def oddEvenList(self, head):
        l=ListNode(0)
        r=ListNode(0)
        l1,r1=l,r
        s=0
        while head:
            s+=1
            if s%2==1:
                l.next=head
                l=head
            else:
                r.next=head
                r=head
            head=head.next
        l.next=r1.next
        r.next=None
        return l1.next

s=Solution()

test=[
{"input":toLinkNode([1,2,3,4,5]),"output":[[1],[2],[3],[],[]]},
{"input":toLinkNode([2,1,3,5,6,4,7]),"output":[[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]},
]


for t in test:
    r=s.oddEvenList(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))