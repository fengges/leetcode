
import functools
def cmp(a,b):
    return a[0]*b[1]-a[1]*b[0]

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        ans=[]
        size=len(arr)
        for i in range(size):
            for j in range(i+1,size):
                ans.append([arr[i],arr[j]])

        ans.sort(key=functools.cmp_to_key(cmp))
        return ans[k-1]