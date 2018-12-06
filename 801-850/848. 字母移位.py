class Solution:
    def shiftingLetters(self, S, shifts):
        r=[]
        sum=0
        for i in range(len(shifts)-1,-1,-1):
            sum+=shifts[i]
            sum%=26
            r.append(sum)
        r.reverse()
        t=''
        for i,s in enumerate(S):
            tmp=ord(s) + r[i]
            if tmp>ord('z'):
                tmp-=26
            t+=chr(tmp)
        return t

s=Solution()
test=[
{"input":["abc",[3,5,9]], "output":True},

]
for t in test:
    r=s.shiftingLetters(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
