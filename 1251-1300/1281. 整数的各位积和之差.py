class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        str1=str(n)
        arr=[int(a) for a in str1]
        ans=1
        for a in arr:
            ans*=a
        return ans-sum(arr)