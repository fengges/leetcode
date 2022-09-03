class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        def fun(num):
            ans=[]
            while num:
                ans.append(num&1)
                num=num>>1
            return ans
        a1,b1,c1=fun(a),fun(b),fun(c)
        size=max(len(a1),len(b1),len(c1))
        a1.extend([0]*(size-len(a1)))
        b1.extend([0]*(size-len(b1)))
        c1.extend([0]*(size-len(c1)))

        ans=0
        for i in range(size):
            if c1[i]==1 and a1[i]==0 and b1[i]==0:
                ans+=1
            elif c1[i]==0 and a1[i]==1 and b1[i]==1:
                ans+=2
            elif c1[i]==0 and (a1[i]==1 or b1[i]==1):
                ans+=1
        return ans


s=Solution()

test=[
    {"input":[2,6,5],"output":3},

]
for t in test:
    r=s.minFlips(*t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))