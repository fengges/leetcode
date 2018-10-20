from util.link import ListNode,toLinkNode

class Solution(object):
    def detectCycle(self, head):
        fast,slow=head,head
        if fast is None or fast.next is None:
            return None
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
            if fast==slow:
                break
        if fast is None or fast.next is None:
            return None
        slow=head
        while slow!=fast:
            slow=slow.next
            fast=fast.next
        return slow
s=Solution()
test=[
{"input":toLinkNode([1,2]), "output":26},
]

for t in test:
    r=s.detectCycle(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))