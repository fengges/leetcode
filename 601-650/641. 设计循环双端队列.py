class MyCircularDeque:
    def __init__(self, k):
        self.deque=[]
        self.k=k

    def insertFront(self, value):
        if len(self.deque)==self.k:
            return False
        self.deque.insert(0,value)
        return True
    def insertLast(self, value):
        if len(self.deque)==self.k:
            return False
        self.deque.append(value)
        return True

    def deleteFront(self):
        if len(self.deque)==0:
            return False
        else:
            del self.deque[0]
            return True

    def deleteLast(self):
        if len(self.deque)==0:
            return False
        else:
            del self.deque[-1]
            return True

    def getFront(self):
        if len(self.deque) == 0:
            return -1
        return self.deque[0]

    def getRear(self):
        if len(self.deque) == 0:
            return -1
        return self.deque[-1]
    def isEmpty(self):
        return  len(self.deque)==0

    def isFull(self):
        return len(self.deque)==self.k