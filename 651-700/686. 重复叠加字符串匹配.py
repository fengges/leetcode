class Solution:
    def repeatedStringMatch(self, A, B):
        tmp=A
        size=int(len(B)/len(A))+2
        for i in range(1,size+1):
            if tmp.find(B)>=0:
                return i
            tmp+=A
        return -1
s=Solution()
test=[
{"input": ["abcd","cdabcdab"], "output":3},

]

for t in test:
    r=s.repeatedStringMatch(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))