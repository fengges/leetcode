class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def nextLargerNodes(self, head):
        t=[]
        while head:
            t.append(head.val)
            head=head.next
        return self.dailyTemperatures(t)
    def dailyTemperatures(self, T):
        stack=[]
        r=[0 for i in range(len(T))]
        for i,v in enumerate(T):
            while len(stack)!=0 and stack[-1][0] < v:
                tmp=stack.pop()
                r[tmp[1]] = v
            stack.append([v, i])
        return r