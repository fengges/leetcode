class MyCalendar:
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
        i=-1
        for i in range(len(self.list)-1):
            if self.list[i][1]<=start and self.list[i+1][0]>=end:
                break
        else:
            if self.list[-1][1]<=start:
                return len(self.list)
            else:
                return -1
        return i+1
s=MyCalendar()


[47,50],[33,41],[39,45],[33,42],[25,32],[26,35],[19,25],[3,8],[8,13],[18,27]
test=[
{"input":[47,50],"output": [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]},
{"input":[33,41],"output": [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]},
{"input":[39,45],"output": [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]},
{"input":[33,42],"output": [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]},
{"input":[25,32],"output": [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]},
{"input":[26,35],"output": [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]},
{"input":[19,25],"output": [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]},
]
for t in test:
    r=s.book(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))