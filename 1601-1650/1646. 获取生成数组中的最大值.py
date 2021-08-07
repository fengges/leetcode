class Solution:
    def getMaximumGenerated(self, n: int) :
        if n<=1:
            return n
        nums=[0]*(n+1)
        nums[1]=1
        for i in range(2,n+1):
            if i%2==0:
                nums[i]=nums[i//2]
            else:
                nums[i]=nums[i//2]+nums[i//2+1]
        return max(nums)
s=Solution()
test=[
    {"input":3, "output":"ababababab"},

]

for t in test:
    r=s.getMaximumGenerated(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))