class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        start = 0
        size=len(gas)
        remain = gas[0] - cost[0]
        stop = (start + 1) % size
        while start != stop:
            if remain < 0:
                start = (start-1+size) % size
                remain += gas[start] - cost[start]
            else:
                remain += gas[stop] - cost[stop]
                stop = (stop+1) % size
        if (remain >= 0):
            return start
        else:
            return -1

s=Solution()
test=[
{"input": [[1,2,3,4,5],[3,4,5,1,2]], "output":3},
{"input": [[1,2,3,4,5],[1,2,3,4,5]], "output":3},
]

for t in test:
    r=s.canCompleteCircuit(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
