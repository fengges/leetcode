class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        if head is None:
            return None

        cur=head
        while cur:
            copy_node=RandomListNode(cur.label)
            copy_node.next=cur.next
            cur.next=copy_node
            cur=copy_node.next
        cur=head
        while cur:
            if cur.random:
                cur.next.random=cur.random.next
            cur=cur.next.next
        cur=head
        old_head=RandomListNode(0)
        new_head=RandomListNode(0)
        cur_new,cur_old=new_head,old_head
        while cur:
            cur_old.next=cur
            cur_old=cur_old.next
            cur_new.next=cur.next
            cur_new= cur.next
            cur=cur.next.next
        cur_new.next=None
        cur_old.next=None
        return new_head.next

a=RandomListNode(-1)
b=RandomListNode(2)
# c=RandomListNode(3)
a.next=b
# a.random=b
# b.random=b
# b.next=c
# c.random=a
s=Solution()
test=[
{"input": a, "output":"IPv4"},
]

for t in test:
    r=s.copyRandomList(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
