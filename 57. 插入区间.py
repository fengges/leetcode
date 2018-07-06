# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def insert(self, intervals, newInterval):
        list=[]
        list.extend(intervals)
        list.append(newInterval)
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