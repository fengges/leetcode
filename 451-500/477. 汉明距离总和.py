class Solution:
    def totalHammingDistance(self, nums):
        tmp=[]
        for i in nums:
            tmp.append(self.get(i))
        num=0
        for i in range(32):
            s=0
            for t in tmp:
                if t[i]==1:
                    s+=1
            num+=s*(len(tmp)-s)
        return num
    def get(self,n):
        tmp=[0 for i in range(32)]
        for i in range(32):
            if n&1==1:
                tmp[i]=1
            n=n>>1
        return tmp

s=Solution()
test=[
{"input": [ 4, 14, 2], "output":6},

]

for t in test:
    r=s.totalHammingDistance(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.totalHammingDistance(t['input'])