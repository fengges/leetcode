
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def toLinkNode(nums,C=False):
    head=ListNode(0)
    temp=head
    for n in nums:
        t = ListNode(n)
        temp.next=t
        temp=t
    if C:
        temp.next=head.next
    return head.next
class Solution:
    def mergeNodes(self, head) :
        ans=[]

        while head:
            if head.val==0:
                ans.append(0)
            else:
                ans[-1]+=head.val
            head=head.next
        if ans[-1]==0:
            ans.pop()


        return toLinkNode(ans,False)

s=Solution()

test=[
    {"input":toLinkNode([0,3,1,0,4,5,2,0]),"output":[13,4]},
    {"input":toLinkNode([0,1,0,3,0,2,2,0]),"output":[13,4]},

]
for t in test:
    r=s.mergeNodes(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))