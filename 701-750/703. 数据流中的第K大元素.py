from util.heap import adjust,buildSmallHeap
def buildSmallHeap(num):
    for i in range(int(len(num)/2),0,-1):
        adjust(num, i)
def adjust(array,i):
    temp = array[i]
    k=i*2
    l=len(array)
    while k<l:
        if k+1 < l and array[k] > array[k + 1]:
            k+=1
        if temp<=array[k]:
            break
        else:
            array[i] = array[k]
            i = k
        k*=2
    array[i] = temp
class KthLargest:
    def __init__(self, k, nums):
        nums.sort()
        self.k=k
        self.nums=nums[max(0,len(nums)-self.k):]
        self.nums.insert(0,0)
    def add(self, val):
        if len(self.nums)<=self.k:
            self.nums.append(val)
            buildSmallHeap(self.nums)
        elif val>self.nums[1]:
            self.nums[1]=val
            adjust(self.nums,1)
        return self.nums[1]
# s=KthLargest(1,[])
# test=[
# {"input": 3, "output":4},
# {"input": 5, "output":5},
# {"input": 10, "output":5},
# {"input": 9, "output":8},
# {"input": 4, "output":8},
# ]
# s=KthLargest(3,[4,5,8,2])
# test=[
# {"input": 3, "output":4},
# {"input": 5, "output":5},
# {"input": 10, "output":5},
# {"input": 9, "output":8},
# {"input": 4, "output":8},
# ]
s=KthLargest(1,[-2])
test=[
{"input": -3, "output":4},
{"input": 0, "output":5},
{"input": 2, "output":5},
{"input": -1, "output":8},
{"input": 4, "output":8},
]
for t in test:
    r=s.add(t['input'])
    print(r)


