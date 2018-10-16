class Solution:
    def findComplement(self, num):
        n=[]
        while num!=0:
            if num&1==1:
                n.append(1)
            else:
                n.append(0)
            num=num>>1
        n=[1-i for i in n]
        n.reverse()
        r=0
        for i in n:
            r=r*2+i
        return r

s=Solution()
test=[
{"input": 2, "output":1},
{"input": 5, "output":2},


]

for t in test:
    r=s.findComplement(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
