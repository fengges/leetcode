class Solution:
    def findRepeatedDnaSequences(self, s):
        length=len(s)
        dic={}
        for i in range(10,length+1):
            t=s[i-10:i]
            if t not in dic:
                dic[t]=0
            dic[t] +=1
        return [k for k in dic if dic[k]>1]
s=Solution()
test=[
{"input":"AAAAAAAAAAA", "output":[]},

]
for t in test:
    r=s.findRepeatedDnaSequences(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))