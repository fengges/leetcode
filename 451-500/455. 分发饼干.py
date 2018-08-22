class Solution:
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        i,j,k=0,0,0
        while i<len(g) and j<len(s):
            if g[i]<=s[j]:
                k+=1
                i+=1
            j+=1
        return k

s=Solution()
test=[
{"input":[[1,2,3], [1,1]], "output":1},
{"input": [ [1,2], [1,2,3]], "output":2},

]

for t in test:
    r=s.findContentChildren(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.findContentChildren(t['input'][0], t['input'][1])