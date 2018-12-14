class MyQueue:
    def __init__(self):
        self.a=[]
        self.b=[]

    def push(self, x):

        self.a.append(x)

    def pop(self):
        print(self.a)
        print(self.b)
        if len(self.b)==0:
            self.b=self.a[::-1]
            self.a=[]
        return self.b.pop()

    def peek(self):
        if len(self.b)==0:
            self.b=self.a[::-1]
            self.a=[]
        return self.b[-1]

    def empty(self):
        print(self.a)
        print(self.b)
        return len(self.a)+len(self.b)==0
t=MyQueue()
t.push(1)
t.push(1)
t.peek()
t.pop()
t.pop()
print(t.empty())