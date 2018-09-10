from util.link import ListNode,toLinkNode
class Solution:
    def numComponents(self, head, G):
        r=0
        dic={k for k in G}
        find=False
        while head:
            if head.val not in dic:
                if find:
                    r+=1
                find=False
            else:
                find=True
            head=head.next
        if find:
            r+=1
        return r
s=Solution()

test=[
{"input":[toLinkNode([0,1,2]),[1,0]],"output":1},
{"input":[toLinkNode([0,1,2,3]),[0, 1, 3]],"output":2},
{"input":[toLinkNode([0,1,2,3,4]),[0, 3, 1, 4]],"output":2},
]


for t in test:
    r=s.numComponents(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
