class Solution:
    def subarraySum(self, nums, k):
        d={0:1}
        s, cnt = 0, 0
        for n in nums:
            s += n
            cnt += d.get(s - k, 0)
            d[s] = d.get(s, 0) + 1

        return cnt


s = Solution()
test = [
    {"input": [[0,0,0,0,0,0,0,0,0,0], 0], "output": 0},
    {"input": [[1],0], "output": 0},
    {"input": [ [1,1,1],2], "output":2},
]

for t in test:
    r = s.subarraySum(t['input'][0],t['input'][1])
    if r != t['output']:
        print("error:" + str(t) + " out:" + str(r))
        r = s.subarraySum(t['input'][0], t['input'][1])


