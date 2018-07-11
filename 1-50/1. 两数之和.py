class Solution:
    def twoSum(self, nums, target):
        for a in nums:
            b=target-a
            if b in nums:
                a_index=nums.index(a)
                if b in nums[0:a_index]:
                    return [a_index,nums[0:a_index].index(b)]
                elif b in nums[a_index+1:]:
                    return [a_index, nums[a_index+1:].index(b)+a_index+1]



s=Solution()
print(s.twoSum([3,2,4],6))


