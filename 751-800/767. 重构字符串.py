class Solution(object):
    def reorganizeString(self, S):
        dic={}
        for s in S:
            if s not in dic:
                dic[s]=0
            dic[s]+=1
        r=""
        while True:
            tmp=[[k,dic[k]] for k in dic if dic[k]>0]
            if len(tmp)==1:
                if tmp[0][1]>1:
                    return ""
                return r+tmp[0][0]
            elif len(tmp)==0:
                return True
            else:
                for k in dic:
                    if dic[k]>0:
                        dic[k]-=1
                        r+=k
s=Solution()
test=[
{"input":"aab", "output":"aba"},
{"input":"aaab", "output":""},
]

for t in test:
    r=s.reorganizeString(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))


