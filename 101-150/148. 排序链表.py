from util.link import ListNode,toLinkNode
class Solution:
    def insertionSortList(self, head):
        sort=ListNode(0)
        while head:
            temp=sort
            while temp.next:
                if temp.next.val>head.val:
                    break
                temp=temp.next
            tmp=head.next
            head.next=temp.next
            temp.next=head
            head=tmp
        return sort.next