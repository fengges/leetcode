class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        ans=[i for i,a in enumerate(nums) if i%10==a]
        return -1 if not ans else ans[0]