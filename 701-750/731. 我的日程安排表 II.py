class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class MyCalendarTwo:
    def __init__(self):
        self.first, self.second=[],[]

    def insert(self, intervals,newInterval):
        newInterval=Interval(newInterval[0],newInterval[1])
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

    def book(self,start,end):
        for  a in self.second:
            if a.end <= start or end <= a.start:
                continue
            else:
                return False
        for  a in  self.first:
            if a.end <= start or end <= a.start:
                continue
            else:
                self.second=self.insert(self.second,[max(a.start, start), min(a.end, end)])
        self.first=self.insert(self.first,[start, end])
        return True


s=MyCalendarTwo()
true=True
false=False
test=[
{"input":[10,20],"output": true},
{"input":[50,60],"output": true},
{"input":[10,40],"output": true},
{"input":[5,15],"output": false},
{"input":[5,10],"output": true},
{"input":[25,55],"output": true},
]
for t in test:
    r=s.book(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))

