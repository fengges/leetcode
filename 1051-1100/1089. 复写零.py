class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        ans=[]
        for a in arr:
            ans.append(a)
            if a==0:
                ans.append(0)
        for i in range(len(arr)):
            arr[i]=ans[i]
    