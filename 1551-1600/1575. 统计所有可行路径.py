class Solution:
    def countRoutes(self, locations, start: int, finish: int, fuel: int) -> int:
        size=len(locations)
        dp=[ [abs(locations[i]-locations[j]) for j in range(size)] for i in range(size)]
        self.ans=0

        def dps(index,f):
            if index==finish:
                self.ans+=1
                self.ans%=(10e9+7)

            for i in range(size):
                if i!=index and dp[index][i]<=f:
                    dps(i,f-dp[index][i])

        dps(start,fuel)
        return self.ans
s=Solution()

test=[
    {"input":[ [1,2,3],0,2,40],"output":6},


]
for t in test:
    r=s.countRoutes(*t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))