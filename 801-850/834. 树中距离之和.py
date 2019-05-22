class Solution:
    def sumOfDistancesInTree(self, N, edges):
        graph=[[] for i in range(N)]
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
        dp=[[0,1] for i in range(N)]
        self.dfs_fill_dp(graph,dp,0,-1)
        ans = [0 for i in range(N)]
        ans[0]=dp[0][0]
        self.fill_ans_array(graph,dp,ans,0, -1, N)
        return ans
    def fill_ans_array(self,graph,dp,ans,root,father,N):
        for i in range(len(graph[root])):
            if graph[root][i] == father:
                continue
            ans[graph[root][i]] = ans[root] + N - 2 * dp[graph[root][i]][1]
            self.fill_ans_array(graph,dp,ans,graph[root][i], root, N)

    def dfs_fill_dp(self,graph,dp,root,father):
        weight_sum,node_sum=0,1
        for i in range(len(graph[root])):
            if graph[root][i]==father:
                continue
            result1,result2=self.dfs_fill_dp(graph,dp,graph[root][i],root)
            weight_sum=weight_sum+result1+result2
            node_sum=node_sum+result2
        dp[root][0]=weight_sum
        dp[root][1]=node_sum
        return dp[root][0],dp[root][1]
s=Solution()
test=[
{"input": [6,[[0,1],[0,2],[2,3],[2,4],[2,5]]], "output":[8,12,6,10,10,10]},
]

for t in test:
    r=s.sumOfDistancesInTree(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
