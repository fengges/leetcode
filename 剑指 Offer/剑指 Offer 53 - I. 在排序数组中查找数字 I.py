class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left =0
        right =len(nums)-1
        count = 0
        while(left<right):
            mid = (left+right)//2
            if(nums[mid]>=target):
                right=mid
            if(nums[mid]<target):
                left = mid+1

        while(left<len(nums) and nums[left]==target):
            count+=1
            left+=1
        return count