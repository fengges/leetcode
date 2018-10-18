class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        start,end=0,0
        left=gas[0]
        size=len(gas)
        while True:
            if left<cost[start]:
                break
            left=left-cost[start]+gas[(start+1)%size]
            start=(start + 1) % size
            if start==end:
                return 0
        end=start
        start=size-1
        while end<=start:
            left=left-cost[start]+gas[(start-1)%size]
            start=(start - 1) % size
        return end
s=Solution()
test=[
{"input": [[1,2,3,4,5],[3,4,5,1,2]], "output":3},
{"input": [[1,2,3,4,5],[1,2,3,4,5]], "output":3},
]

for t in test:
    r=s.canCompleteCircuit(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
