class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        size=len(releaseTimes)
        releaseTimes.insert(0,0)
        ans=[float('-inf'),keysPressed[0]]
        for i in range(size):
            t= releaseTimes[i+1]-releaseTimes[i]
            if t>ans[0]:

                ans[0]=t
                ans[1]=keysPressed[i]
            elif t==ans[0]:
                ans[1]=max(ans[1],keysPressed[i])
        return ans[1]