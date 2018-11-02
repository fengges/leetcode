class MyStack:
    def __init__(self):
        self.list=[]
    def push(self, x):
        self.list.append(x)

    def pop(self):
        t=self.list[-1]
        del self.list[-1]
        return t
    def top(self):
        return self.list[-1]

    def empty(self):
        return len(self.list)==0