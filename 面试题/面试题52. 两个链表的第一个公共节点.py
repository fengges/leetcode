
from util.link import *
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        dict=set()
        while headA:
            dict.add(headA)
            headA=headA.next
        while headB:
            if headB in dict:
                return headB
            headB=headB.next
        return None
        pass