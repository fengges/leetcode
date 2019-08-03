class Solution:
    def findTargetSumWays(self, nums, S):
        sum_nums = sum(nums)
        if sum_nums < S or (S + sum_nums) % 2 != 0:
            return 0
        target = (S + sum_nums) >> 1
        mem = [0] * (target + 1)
        mem[0] = 1
        for num in nums:
            for i in range(target, num - 1, -1):
                mem[i] += mem[i - num]
        return mem[target]


s=Solution()
test=[
{"input":[[5,5,10,2,3],15], "output":5},

]
for t in test:
    r=s.findTargetSumWays(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))