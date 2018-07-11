import copy
class Solution:
    def permuteUnique(self, nums):
        t = []
        self.result = []
        self.dic={}
        index = [False for i in range(len(nums))]
        self.isSelect(index, nums, t)
        return self.result

    def isSelect(self, index, nums, t):
        if self.count(index) == len(nums):
            k=str(t)
            if k not in self.dic:
                self.result.append(copy.deepcopy(t))
                self.dic[k]=""
            return
        for i in range(len(index)):
            if not index[i]:
                index[i] = True
                t.append(nums[i])
                self.isSelect(index, nums, t)
                del t[-1]
                index[i] = False

    def count(self, index):
        num = 0
        for i in index:
            if i:
                num += 1
        return num

s = Solution()

test = [
    {"input": [1], "output": [
        [1]
    ]},
    {"input": [1, 1, 2], "output": [
        [1, 1, 2],
        [1, 2, 1],
        [2, 1, 1]
    ]},

]

for t in test:
    r = s.permuteUnique(t['input'])
    if r != t['output']:
        print("error:" + str(t) + " out:" + str(r))
        r = s.permuteUnique(t['input'])

