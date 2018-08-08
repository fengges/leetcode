
class Solution:
    def findMinDifference(self, timePoints):
        timePoints.sort()
        min=10000000
        size=len(timePoints)
        for i in range(size):
            if (i + 1) == size:
                tmp=self.gap(timePoints[0],timePoints[i],True)
            else:
                tmp = self.gap(timePoints[i+1], timePoints[i],False)
            if tmp<min:
                min=tmp
        return min
    def gap(self,time2,time1,r=False):
        item1=time1.split(":")
        item2=time2.split(":")
        if not r:
            gap=(int(item2[0])-int(item1[0]))*60+int(item2[1])-int(item1[1])
        else:
            gap = (int(item2[0])+24 - int(item1[0])) * 60 + int(item2[1]) - int(item1[1])
        return gap

s = Solution()
test = [

    {"input": ["12:12","12:13"], "output":1},
    {"input":["23:59","00:00","00:50"], "output":1},
]

for t in test:
    r = s.findMinDifference(t['input'])
    if r != t['output']:
        print("error:" + str(t) + " out:" + str(r))
        r = s.findMinDifference(t['input'])
