class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        dic={}
        while headA :
            dic[headA]=1
            headA=headA.next
        while headB:
            if headB in dic:
               break
            headB=headB.next
        return headB

