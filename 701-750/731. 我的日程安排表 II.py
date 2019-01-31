class MyCalendarTwo:
    def __init__(self):
        self.list=[[0,0]]
    def book(self, start, end):
        index=self.find(start,end)
        if index==-1:
            return False
        else:
            self.list.insert(index,[start,end])
            return True
    def find(self,start, end):
        i=0
        for i in range(len(self.list)-1):
            if self.list[i][1]<=start and self.list[i+1][0]>end:
                break
        if i==len(self.list)-1:
            if self.list[-1][1]<=start:
                return i+1
            else:
                return -1
        elif i==len(self.list)-2:
            if self.list[-1][1]<=start:
                return i+1
            else:
                return -1
        else:
            return i+1


MyCalendarTwo()

s=MyCalendarTwo()

test=[
{"input":[10,20],"output": [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]},
{"input":[50,60],"output": [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]},
{"input":[10,40],"output": [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]},
{"input":[5,15],"output": [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]},
{"input":[5,10],"output": [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]},
{"input":[25,55],"output": [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]},
]
for t in test:
    r=s.book(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))

