from util.link import ListNode,toLinkNode

class Solution(object):
    def hasCycle(self, head):
        node1=head
        node2=head
        while node1 is not None and node2 is not None:
            node1=node1.next
            if node2.next is None:
                node2=node2.next
                break
            node2=node2.next.next
            if node1 is not None and node1==node2:
                break
        if node1 is None or node2 is None:
            return False
        else:
            return True

s=Solution()

test=[

{"input":toLinkNode([1,2,3,4,5]),"output":True},

]


for t in test:
    r=s.hasCycle(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        # r = s.reverseBetween(t['input'][0], t['input'][1], t['input'][2])