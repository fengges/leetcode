
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        self.pre=None
        self.num=1

class AllOne:

    def __init__(self):
        self.dicts={}

        self.head=Node('')
        self.head.num=float('-inf')
        self.tail=Node('')
        self.tail.num=float('inf')
        self.head.next=self.tail
        self.tail.pre=self.head


    def inc(self, key: str) -> None:
        if key in self.dicts:
            tmp=self.dicts[key]
            tmp.num+=1
            while tmp.next and tmp.num>tmp.next.num:

                tmp2=tmp.next

                tmp.pre.next=tmp2
                tmp2.pre=tmp.pre

                tmp2.next.pre=tmp
                tmp.next=tmp2.next
                tmp2.next=tmp
                tmp.pre=tmp2

        else:
            tmp=Node(key)
            self.dicts[key]=tmp
            self.head.next.pre=tmp
            tmp.next=self.head.next
            self.head.next=tmp
            tmp.pre=self.head


    def dec(self, key: str) -> None:
        if key in self.dicts:
            tmp=self.dicts[key]
            tmp.num-=1
            if tmp.num!=0:
                while tmp.pre and tmp.num<tmp.pre.num:

                    tmp2=tmp.pre

                    tmp.next.pre=tmp2
                    tmp2.next=tmp.next

                    tmp2.pre.next=tmp
                    tmp.pre=tmp2.pre
                    tmp2.pre=tmp
                    tmp.next=tmp2
            else:
                tmp.next.pre=tmp.pre
                tmp.pre.next=tmp.next
                del tmp


    def getMaxKey(self) -> str:
        return  self.tail.pre.val


    def getMinKey(self) -> str:
        return  self.head.next.val

