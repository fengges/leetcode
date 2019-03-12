class RecentCounter:
    def __init__(self):
        self.list=[]
    def ping(self, t):
        self.list.append(t)
        while self.list[-1]-3000>self.list[0]:
            self.list.pop(0)
        return len(self.list)
