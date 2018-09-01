class KthLargest:
    def __init__(self, k, nums):
        nums.sort(reverse=True)
        self.k=k
        self.nums=nums[0:self.k]

    def add(self, val):
        self.nums.append(val)
        low = 0
        hight = len(self.nums) - 2
        i=hight+1
        while low <= hight:
            mid = int((low + hight) / 2)
            if val < self.nums[mid]:
                low = mid + 1
            else:
                hight = mid - 1
        # 跳出循环后 low, mid 都是一样的, hight = low - 1
        for j in range(i, low, -1):
            self.nums[j] = self.nums[j - 1]
        self.nums[low] = val
        if len(self.nums)>self.k:
            del self.nums[-1]
        return self.nums[-1]
# s=KthLargest(1,[])
# test=[
# {"input": 3, "output":4},
# {"input": 5, "output":5},
# {"input": 10, "output":5},
# {"input": 9, "output":8},
# {"input": 4, "output":8},
# ]
s=KthLargest(3,[4,5,8,2])
test=[
{"input": 3, "output":4},
{"input": 5, "output":5},
{"input": 10, "output":5},
{"input": 9, "output":8},
{"input": 4, "output":8},
]
# s=KthLargest(1,[-2])
# test=[
# {"input": -3, "output":4},
# {"input": 0, "output":5},
# {"input": 2, "output":5},
# {"input": -1, "output":8},
# {"input": 4, "output":8},
# ]
for t in test:
    r=s.add(t['input'])
    print(r)


