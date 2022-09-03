class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        size=len(nums)
        result=[]
        for i in range(size):
            ans=[nums[i]]
            for j in range(j+1,size):
                if nums[j]%nums[i]==0:
                    ans.append(nums[j])
            result=max(ans,result,key=len)
        return result