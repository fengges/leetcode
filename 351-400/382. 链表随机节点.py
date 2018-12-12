import random
class Solution:
    def __init__(self, head):
        self.list=[]
        while head:
            self.list.append(head.val)
            head=head.next
    def getRandom(self):
        return self.list[random.randint(0,len(self.list)-1)]
