class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        ans=[]
        for i,v in enumerate(index):
            ans.insert(v,nums[i])
        return ans