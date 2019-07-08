class Solution:
    def increasingTriplet(self, nums):
        a=b=0x7fffffff
        for n in nums:
            if n<=a:
                a=n
            elif n<=b:
                b=n
            else:
                return True
        return False
s=Solution()
test=[
{"input":[3,4,1,5] , "output":True},
]
for t in test:
    r=s.increasingTriplet(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))