# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals):
        list=intervals
        if  len(list)==0:
            return[]
        list=sorted(list, key=lambda interval: interval.start)
        r=[list[0]]
        for i in range(1,len(list)):
            if list[i].start<=r[-1].end:
                t=Interval(min(r[-1].start,list[i].start),max(list[i].end,r[-1].end))
                del r[-1]
                r.append(t)
            else:
                t = Interval(list[i].start, list[i].end)
                r.append(t)
        return r

s=Solution()

test=[
{"input":[Interval(1,4),Interval(0,0)],"output":[Interval(0,4)]},
{"input":[Interval(1,4),Interval(0,4)],"output":[Interval(0,4)]},
{"input":[],"output":[Interval(1,5)]},
{"input":[Interval(1,3),Interval(2,6),Interval(8,10),Interval(15,18)],"output":[Interval(1,6),Interval(8,10),Interval(15,18)]},
{"input":[Interval(1,4),Interval(4,5)],"output":[Interval(1,5)]},
]

for t in test:
    r=s.merge(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.merge(t['input'])