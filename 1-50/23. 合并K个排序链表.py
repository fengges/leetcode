class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        h = ListNode(0)
        t = h
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                t.next = l1
                t = l1
                l1 = l1.next
            else:
                t.next = l2
                t = l2
                l2 = l2.next
        if l1 is None:
            temp = l2
        else:
            temp = l1
        while temp is not None:
            t.next = temp
            t = temp
            temp = temp.next
        return h.next
    def mergeKLists(self, lists):
        if len(lists)==0:
            return None
        # temp=lists[0]
        # for  i in range(1,len(lists)):
        #     temp=self.mergeTwoLists(lists[i],temp)
        # return temp
        nums=[]
        for link in lists:
            while link is not None:
                nums.append(link.val)
                link=link.next
        nums.sort()
        head=ListNode(0)
        t=head
        for n in nums:
            temp=ListNode(n)
            t.next=temp
            t=temp
        return head.next
