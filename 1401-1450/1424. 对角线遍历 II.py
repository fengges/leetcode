
import functools
def cmp(a,b):
    if a[0]==b[0]:
        return a[1]-b[1]
    else:
        return a[0]-b[0]

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        ans=[]
        for i,n in enumerate(nums):
            for j,v in enumerate(n):
                ans.append([i,j])
        tmp=sorted(ans,key=functools.cmp_to_key(cmp))
        return [nums[t[0]][t[1]] for t in tmp]
