class RecentCounter:

    def __init__(self):
        self.list=[]
        self.index=0

    def ping(self, t: int) -> int:
        self.list.append(t)
        while True:
            if self.list[self.index]<t-3000:
                self.index+=1
            else:
                break
        return len(self.list)-self.index