
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head, m, n):
        temp1=ListNode(0)
        temp1.next=head
        head=temp1
        for i in range(0,m-1):
            head=head.next
        tail=head
        t1=tail.next
        t2=tail.next.next
        tail2=t1
        temp=t2
        for i in range(0,n-m):
            temp=t2.next
            t2.next=t1
            t1 = t2
            t2=temp
        tail.next=t1
        tail2.next=temp
        return temp1.next

def toLinkNode(nums):
    head=ListNode(0)
    temp=head
    for n in nums:
        t = ListNode(n)
        temp.next=t
        temp=t
    return head.next
s=Solution()

test=[
{"input":[toLinkNode([3,5]),1,1],"output":2},
{"input":[toLinkNode([3,5]),1,2],"output":2},
{"input":[toLinkNode([1,2,3,4,5]),2,4],"output":2},

{"input":[toLinkNode([5]),1,1],"output":2},


]
for t in test:
    r=s.reverseBetween(t['input'][0],t['input'][1],t['input'][2])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        # r = s.reverseBetween(t['input'][0], t['input'][1], t['input'][2])




