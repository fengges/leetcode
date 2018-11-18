import copy
class Solution:
    def partition(self, s):
        dp=[[False for i in s] for j in s]
        size=len(s)
        for i in range(size):
            dp[i][i]=True
        for i in range(size-1):
            if s[i+1]==s[i]:
                dp[i][i+1]=True
        for i in range(2,size+1):
            for j in range(size-i):
                dp[j][j+i]= dp[j+1][i+j-1] and s[i+j]==s[j]
        r=[]
        self.find(s,0,size,dp,r,[])
        return r
    def find(self,s,start,end,dp,r,path):
        if start>=end:
            r.append(copy.deepcopy(path))
        for i in range(start,end):
            if dp[start][i]:
                path.append(s[start:i+1])
                self.find(s,i+1,end,dp,r,path)
                del path[-1]
s=Solution()
test=[
{"input":"cbbbcc", "output":[["a","b","b","a","b"],["a","b","bab"],["a","bb","a","b"],["abba","b"]]},
{"input":"abbab", "output":[["a","b","b","a","b"],["a","b","bab"],["a","bb","a","b"],["abba","b"]]},
{"input":"aab", "output":[["aa","b"],["a","a","b"]]},
]
for t in test:
    r=s.partition(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))


