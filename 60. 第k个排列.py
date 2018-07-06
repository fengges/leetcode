class Solution:
    def getPermutation(self, n, k):
        k-=1
        nums=[i for i in range(1,n+1)]
        sum=1
        fact=[]
        for i in range(1,n+1):
            sum*=i
            fact.append(sum)
        result=[]
        fact.reverse()
        lens=len(nums)
        for i in range(lens-1):
            n=int(k/fact[i+1])
            result.append(nums[n])
            del nums[n]
            k-=n*fact[i+1]

        result.extend(nums)
        r=[ str(i) for i in result]
        return "".join(r)


s=Solution()
test=[
{"input": [3,1], "output": 213},



]

for t in test:
    r=s.getPermutation(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.getPermutation(t['input'][0], t['input'][1])