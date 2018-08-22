class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class SummaryRanges:
    def __init__(self):
        self.result=[]

    def addNum(self, val):
        if len(self.result)==0:
            self.result.append(Interval(val,val))
        else:
            index=self.find(val)
            if index==-1:
                if self.result[-1].end+1<val:
                    self.result.append(Interval(val, val))
                elif self.result[-1].end+1==val:
                    self.result[-1].end=val
            elif index==0:
                if self.result[0].start-1>val:
                    self.result.insert(0,Interval(val, val))
                elif self.result[0].start-1==val:
                    self.result[0].start = val
            else:
                if self.result[index].start-1>val and self.result[index-1].end+1<val:
                    self.result.insert(index,Interval(val, val))
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
    def getIntervals(self):
        return self.result

s=SummaryRanges()
test=[
{"input": 1, "output":[[1, 1]]},
{"input": 3, "output":[[1, 1]]},
{"input": 7, "output":[[1, 1]]},
{"input": 2, "output":[[1, 1]]},
{"input": 6, "output":[[1, 1]]},
]

for t in test:
    s.addNum(t['input'])
    t=s.getIntervals()
    print(t)