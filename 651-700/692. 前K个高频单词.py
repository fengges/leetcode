import operator as op
class Solution:
    def reversed_cmp(self,x, y):
        if x[1] > y[1]:
            return -1
        elif x[1] == y[1]:
            if op.lt(x[0], y[0]):
                return -1
            else:
                return 1
        return 1
    def bubbleSort(self,nums):
        for i in range(len(nums) - 1):  # 这个循环负责设置冒泡排序进行的次数
            for j in range(len(nums) - i - 1):  # ｊ为列表下标
                if self.reversed_cmp(nums[j],nums[j + 1])>0:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums
    def topKFrequent(self, words, k):
        dic={}
        for n in words:
            if n not in dic:
                dic[n]=0
            dic[n]+=1
        res=self.bubbleSort(list(dic.items()))
        res=res[0:k]
        r=[]
        for re in res:
            r.append(re[0])
        return r



s = Solution()
test = [
{"input": [["i", "love", "leetcode", "i", "love", "coding"],3], "output": ["i","love","coding"]},
    {"input": [["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4],
     "output": ["the", "is", "sunny", "day"]},
{"input": [["i", "love", "leetcode", "i", "love", "coding"],2], "output": ["i", "love"]},

]

for t in test:
    r = s.topKFrequent(t['input'][0],t['input'][1])
    if r != t['output']:
        print("error:" + str(t) + " out:" + str(r))
        r = s.topKFrequent(t['input'][0], t['input'][1])
