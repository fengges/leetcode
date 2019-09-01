import collections
class Solution:
    def findItinerary(self, tickets):
        dict= collections.defaultdict(list)
        for f, t in tickets:
            dict[f] += [t]
        for k in dict:
            dict[k].sort()
        ans=[]
        def dfs(f):
            while dict[f]:
                dfs(dict[f].pop(0))
            ans.insert(0,f)
        dfs("JFK")
        return ans
s=Solution()
test=[
{"input":[["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]], "output":["JFK","ATL","JFK","SFO","ATL","SFO"]},
{"input":[["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]], "output":["JFK", "MUC", "LHR", "SFO", "SJC"]},
]

for t in test:
    r=s.findItinerary(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))