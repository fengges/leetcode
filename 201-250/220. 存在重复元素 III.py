class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if len(nums) == 0 or t < 0 or k < 0:
            return False
        from collections import defaultdict
        t += 1
        record = {}
        for i, c in enumerate(nums):
            if i > k and nums[i - k - 1] // t in record:
                # 新的窗口内一定没有桶nums[i-k-1]//t里的数
                # 否则在遍历到nums[i-k-1]就会返回真
                record.pop(nums[i - k - 1] // t)
            if c // t in record or (c // t - 1 in record and c - record[c // t - 1] < t) or (
                            c // t + 1 in record and record[c // t + 1] - c < t):
                return True
            # 此处record里一定没有c//t
            # 否则前面会返回真
            record[c // t] = c
        return False


s=Solution()
test=[
{"input": [[1,2,3,1],  3, 0], "output":"B7H11He49Li20N47O35"},
]

for t in test:
    r=s.containsNearbyAlmostDuplicate(t['input'][0],t['input'][1],t['input'][2])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
