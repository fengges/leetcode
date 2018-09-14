class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
class Solution(object):
    def flatten(self, head):
        t=head
        while head:
            if head.child:
                tmp=head.next
                c=self.flatten(head.child)
                head.next=c
                c.prev=head
                head.child=None
                while c.next:
                    c=c.next
                c.next=tmp
                if tmp is not None:
                    tmp.prev=c
            head=head.next
        return t
    def flatten2(self, head):
        l=[]
        while head:
            l.append(head['val'])
            if head['child']:
                l.extend(self.flatten2(head['child']))
            head=head['next']
        return l
null=None  
t=eval('{"val":"1","child":null,"next":{"val":"2","child":null,"next":{"val":"3","child":{"val":"7","child":null,"next":{"val":"8","child":{"val":"11","child":null,"next":{"val":"12","child":null,"next":null,"prev":{"$ref":"11"},"val":12},"prev":null,"val":11},"next":{"val":"9","child":null,"next":{"val":"10","child":null,"next":null,"prev":{"$ref":"9"},"val":10},"prev":{"$ref":"8"},"val":9},"prev":{"$ref":"7"},"val":8},"prev":null,"val":7},"next":{"val":"4","child":null,"next":{"val":"5","child":null,"next":{"val":"6","child":null,"next":null,"prev":{"$ref":"5"},"val":6},"prev":{"$ref":"4"},"val":5},"prev":{"$ref":"3"},"val":4},"prev":{"$ref":"2"},"val":3},"prev":{"$ref":"1"},"val":2},"prev":null,"val":1}')
s=Solution()

r=s.flatten2(t)
print(r)
