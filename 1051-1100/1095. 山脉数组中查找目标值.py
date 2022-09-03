class MountainArray:
    def __init__(self,arr):
        self.arr=arr
    def get(self, index: int) -> int:
       return self.arr[index]
    def length(self) -> int:
        return len(self.arr)

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        def binary_search(mountain, target, l, r, key=lambda x: x):
            target = key(target)
            while l <= r:
                mid = (l + r) // 2
                cur = key(mountain.get(mid))
                if cur == target:
                    return mid
                elif cur < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1

        size=mountain_arr.length()
        l,r=0,size-1
        while l < r:
            mid = (l + r) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                l = mid + 1
            else:
                r = mid
        peak = l
        print(l)
        index = binary_search(mountain_arr, target, 0, peak)
        if index != -1:
            return index
        index = binary_search(mountain_arr, target, peak + 1, mountain_arr.length() - 1,lambda x: -x)
        return index

s=Solution()

test=[
    {"input":[1,MountainArray([0,5,3,1])],"output":3},


]
for t in test:
    r=s.findInMountainArray(*t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))