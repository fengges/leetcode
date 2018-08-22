class Solution:
    class Interval:
        def __init__(self, s=0, e=0):
            self.start = s
            self.end = e
    def longestConsecutive(self, nums):
        self.result=[]
        for n in nums:
            self.addNum(n)
        maxL=0
        for r in self.result:
            L=r.end-r.start+1
            maxL=max(maxL,L)
        return maxL

    def addNum(self, val):
        if len(self.result)==0:
            self.result.append(Solution.Interval(val,val))
        else:
            index=self.find(val)
            if index==-1:
                if self.result[-1].end+1<val:
                    self.result.append(Solution.Interval(val, val))
                elif self.result[-1].end+1==val:
                    self.result[-1].end=val
            elif index==0:
                if self.result[0].start-1>val:
                    self.result.insert(0,Solution.Interval(val, val))
                elif self.result[0].start-1==val:
                    self.result[0].start = val
            else:
                if self.result[index].start-1>val and self.result[index-1].end+1<val:
                    self.result.insert(index,Solution.Interval(val, val))
                elif self.result[index].start-1>val and self.result[index-1].end+1==val:
                    self.result[index - 1].end=val
                elif self.result[index].start-1==val and self.result[index-1].end+1<val:
                    self.result[index].start=val
                elif self.result[index].start-1==val and self.result[index-1].end+1==val:
                    self.result[index-1].end=self.result[index].end
                    del self.result[index]


    def find(self,val):
        for i,value in enumerate(self.result):
            if value.start>=val:
                return i
        return -1

s=Solution()
test=[
{"input":[100, 4, 200, 1, 3, 2], "output":4},
{"input":[0,-1], "output":2},

]

for t in test:
    r=s.longestConsecutive(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.longestConsecutive(t['input'])
