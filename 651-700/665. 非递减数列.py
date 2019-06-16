class Solution:
    def checkPossibility(self, nums):
        index=-1
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1] and index==-1:
                index=i
            elif nums[i]>nums[i+1]:
                return False
        if index<=0 or index+2==len(nums):
            return True
        elif nums[index-1]<=nums[index+1]:
            return True
        elif index+2<len(nums) and nums[index+2]>=nums[index]:
            return True
        else:
            return False

s = Solution()
test = [
{"input": [-1,4,2,3], "output": True},
{"input": [1,2,4,5,3], "output": True},
{"input": [2,3,3,2,4], "output": True},
{"input": [3,4,2,3], "output": False},
{"input": [1,5,4,6,7,10,8,9], "output": False},
{"input": [4,2,1], "output": False},
{"input": [4,2,3], "output": True},

]

for t in test:
    r = s.checkPossibility(t['input'])
    if r != t['output']:
        print("error:" + str(t) + " out:" + str(r))
        r = s.checkPossibility(t['input'])