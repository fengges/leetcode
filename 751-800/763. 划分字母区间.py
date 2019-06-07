class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
class Solution:
    def partitionLabels(self, S):
        dict={}
        for i,s in enumerate(S):
            if s not in dict:
                dict[s]=[]
            dict[s].append(i)
        intervals=[Interval(dict[s][0],dict[s][-1])  for s in dict]
        r=self.merge(intervals)
        t=[ i.end-i.start+1  for i in r]
        return t
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
