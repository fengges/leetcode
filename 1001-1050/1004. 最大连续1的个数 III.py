class Solution:
    def longestOnes(self, nums, k: int) -> int:
        l=-1
        ans=0
        result=0
        for i,n in enumerate(nums):
            if n==0:
                while result>=k:
                    l+=1
                    if nums[l]==0:
                        result-=1
                result+=1
                ans=max(ans,i-l)
            else:
                ans=max(ans,i-l)
        return ans

s=Solution()

test=[
    {"input":[ [1,1,1,0,0,0,1,1,1,1,0],2],"output":6},


]
for t in test:
    r=s.longestOnes(*t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
