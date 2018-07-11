class Solution:
    def climbStairs(self, n):
        if n<=2:
            return n
        step=[0,1,2]
        for i in range(3,n+1):
            step.append(step[i-1]+step[i-2])
        return step[n]