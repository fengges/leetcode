class MyCircularQueue:
    def __init__(self, k):
        self.queue = [0 for i in range(k + 1)]
        self.s = 0
        self.e = 0
        self.k = k + 1

    def enQueue(self, value):
        if self.e == (self.s + 1) % self.k:
            return False
        else:
            self.queue[self.s] = value
            self.s = (self.s + 1) % self.k
            return True

    def deQueue(self):
        if self.e == self.s:
            return False
        else:
            self.e = (self.e + 1) % self.k
            return True

    def Front(self):
        if self.e == self.s:
            return -1
        else:
            return self.queue[self.e]

    def Rear(self):
        if self.e == self.s:
            return -1
        else:
            return self.queue[(self.s - 1) % self.k]

    def isEmpty(self):
        return self.e == self.s

    def isFull(self):
        return self.e == (self.s + 1) % self.k