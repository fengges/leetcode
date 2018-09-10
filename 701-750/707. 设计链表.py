from util.link import ListNode,toLinkNode
class MyLinkedList:
    def __init__(self):
        self.head=ListNode(0)
        self.tail=self.head

    def get(self, index):
        h=self.head.next
        now=0
        while h:
            if index==now:
                return h.val
            h=h.next
            now+=1
        return -1

    def addAtHead(self, val):
        self.addAtIndex(0, val)

    def addAtTail(self, val):
        temp=ListNode(val)
        self.tail.next=temp
        self.tail=temp

    def addAtIndex(self, index, val):
        h=self.head
        now=0
        while h:
            if index==now:
                break
            h=h.next
            now+=1
        if h is not None:

            temp=ListNode(val)
            temp.next=h.next
            h.next=temp
            if temp.next is None:
                self.tail=temp



    def deleteAtIndex(self, index):
        h=self.head
        now=0
        while h:
            if index==now:
                break
            h=h.next
            now+=1
        if h and h.next:
            if h.next==self.tail:
                self.tail=h
            h.next=h.next.next

["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]
[[],[1],[3],[1,2],[1],[1],[1]]

s=MyLinkedList()
t=s.addAtHead(1)
t=s.addAtTail(3)
t=s.addAtIndex(1,2)
t=s.get(1)
t=s.deleteAtIndex(1)
t=s.get(1)

["MyLinkedList","addAtHead","get","addAtTail","deleteAtIndex",
 "addAtHead","deleteAtIndex","get","addAtTail","addAtHead",
 "addAtTail","addAtTail","addAtTail","addAtIndex","get",
 "addAtTail"]
[[],[8],[1],[81],[2],
 [26],[2],[1],[24],[15],
 [0],[13],[1],[6,33],[6],
 [2,91]]

s=MyLinkedList()
t=s.addAtHead(8)
t=s.get(1)
t=s.addAtTail(81)
t=s.deleteAtIndex(2)

t=s.addAtHead(26)
t=s.deleteAtIndex(2)
t=s.get(1)
t=s.addAtTail(24)
t=s.addAtHead(15)

t=s.addAtTail(0)
t=s.addAtTail(13)
t=s.addAtTail(1)
t=s.addAtIndex(6,33)
t=s.get(6)
print(t)

