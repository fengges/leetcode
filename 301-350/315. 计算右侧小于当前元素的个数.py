class Solution:
    def countSmaller(self, nums):

        if not nums or not len(nums):
            return []
        tmp = []
        res = []
        for i in reversed(nums):
            pos = self.bisert(tmp, i)
            res.append(pos)
        return list(reversed(res))

    def bisert(self, tmp, t):
        start = 0
        end = len(tmp) - 1
        while end >= start:
            mid = (start + end) >> 1
            if tmp[mid] > t:
                end = mid - 1
            else:
                start = mid + 1
        index = start - 1
        while index >= 0 and tmp[index] == t:
            index -= 1
        tmp.insert(index + 1, t)
        return index + 1

s=Solution()
test=[
{"input":[5,2,6,1], "output":[2,1,1,0] },

]
for t in test:
    r=s.countSmaller(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))