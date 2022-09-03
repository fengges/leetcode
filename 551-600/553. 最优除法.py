class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        nums=[str(n)+'/' for n in nums]
        nums[-1]=nums[-1].strip('/')
        if len(nums)>2:
            nums.insert(1,'(')
            nums.append(')')
        return ''.join(nums)