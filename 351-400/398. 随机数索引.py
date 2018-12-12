import random
class Solution:
    def __init__(self, nums):
        self.dic={}
        for i,n in enumerate(nums):
            if n not in self.dic:
                self.dic[n]=[]
            self.dic[n].append(i)

    def pick(self, target):
        tmp=self.dic[target]
        return tmp[random.randint(0,len(tmp)-1)]

