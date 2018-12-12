import random
class Solution:
    def __init__(self, N, blacklist):
        self.size=N-len(blacklist)
        self.dic={b:-1 for b in blacklist}
        for b in blacklist:
            if b<self.size:
                while N-1 in self.dic:
                    N-=1
                self.dic[b]=N-1
                N-=1
        print(self.size)
        print(self.dic)


    def pick(self):
        t=random.randint(0,self.size-1)
        if t in self.dic:
            return self.dic[t]
        else:
            return t
