class Solution:
    def minCostClimbingStairs(self, cost):
        cost.append(0)
        path=[0 for c in cost]
        path[0]=cost[0]
        path[1] = cost[1]
        for i in range(2,len(cost)):
            path[i]=min(path[i-1],path[i-2])+cost[i]
        return path[-1]