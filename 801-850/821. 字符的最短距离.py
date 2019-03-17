class Solution:
    def shortestToChar(self, S, C) :
        index=[i for i in range(len(S)) if S[i]==C]
        index.insert(0,float("-inf"))
        index.append(float("inf"))
        start=0
        res=[]
        for i,v in enumerate(S):
            if v==C:
                start+=1
                res.append(0)
            else:
                res.append(min(i-index[start],index[start+1]-i))
        return res
s=Solution()

test=[
{"input":["loveleetcode","e"],"output":True},
]


for t in test:
    r=s.shortestToChar(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
