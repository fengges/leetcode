class Solution:
    def countMaxOrSubsets(self, nums) -> int:
        maxa=0
        for n in nums:
            maxa|=n


        def fun(index,a):
            ans=0
            if index==len(nums):
                return ans
            # if a==maxa:
            #     ans+=1
            b=a|nums[index]
            if b==maxa:
                ans+=1
            return ans+fun(index+1,a)+fun(index+1,b)

        return fun(0,0)

s=Solution()
test=[
    {"input":  [3,1],"output":2},

]

for t in test:
    r=s.countMaxOrSubsets(t['input'] )
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))