from util.link import ListNode,toLinkNode
class Solution:
    def reorderList(self, head):
        if head is None:
            return None
        tmp=ListNode(0)
        tmp.next=head
        fast,slow=tmp,tmp
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        min=slow
        slow=slow.next
        stack=[]
        while slow:
            stack.append(slow)
            slow=slow.next
        stack.reverse()
        for s in stack:
            s.next=head.next
            head.next=s
            head=s.next
        head.next=None
        head=tmp.next
s=Solution()
test=[
{"input": toLinkNode([1,2,3,4,5]), "output":"IPv4"},
{"input": toLinkNode([1,2,3,4]), "output":"IPv4"},
]

for t in test:
    r=s.reorderList(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))




