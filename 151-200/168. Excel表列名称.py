class Solution:
    def convertToTitle(self, n):
        s=[]
        while n!=0:
            s.append(chr((n-1)%26+ord("A")))
            n=int((n-1)/26)
        s.reverse()
        return ''.join(s)
s=Solution()
test=[
{"input":26, "output":"Z"},

]

for t in test:
    r=s.convertToTitle(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.convertToTitle(t['input'])
