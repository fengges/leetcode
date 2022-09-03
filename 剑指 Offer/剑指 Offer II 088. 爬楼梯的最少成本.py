class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.insert(0,0)
        cost.insert(0,0)
        cost.append(0)
        flag=[float('inf') for c in range(len(cost))]
        flag[0]=0
        flag[1]=0
        for i in range(2,len(flag)):
            flag[i]=min(flag[i-1],flag[i-2])+cost[i]
        return flag[-1]