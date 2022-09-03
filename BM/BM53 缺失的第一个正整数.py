#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param nums int整型一维数组
# @return int整型
#
class Solution:
    def minNumberDisappeared(self , nums) -> int:
        # write code here
        size=len(nums)
        for n in nums:
            if n>0 and n<size:
                nums[n]=0
        for i,n in enumerate(nums):
            if n:
                return i
        return size
s=Solution()

test=[
    {"input":    [-2,3,4,1,5],"output":2},

]
for t in test:
    r=s.minNumberDisappeared(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
