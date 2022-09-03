class MinStack:
    def __init__(self):
        self.stack=[]
        self.min=[]
    def push(self, x):
        self.stack.append(x)
        if len(self.min)==0 or self.min[-1]>=x:
            self.min.append(x)
    def pop(self):
        if len(self.stack)!=0:
            if self.stack[-1]==self.min[-1]:
                del self.min[-1]
            del self.stack[-1]
    def top(self):
        return self.stack[-1]

    def min(self):
        return self.min[-1]