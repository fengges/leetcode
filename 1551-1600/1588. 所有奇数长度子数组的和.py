class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans=[0]
        for a in arr:
            ans.append(ans[-1]+a)

        r=0
        size=len(arr)
        for i in range(size):
            for j in range(i,size,2):
                r+=ans[j+1]-ans[i]
                # print(i,j,ans[j+1]-ans[i])
        return r