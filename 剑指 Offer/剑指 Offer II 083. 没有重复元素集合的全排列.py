class Solution:
    def permute(self, nums):
        flag=[True for n in nums]
        ans=[]
        def fun(n,tmp):
            if n==len(nums):
                ans.append([t for t in tmp])
            for i,f in enumerate(flag):
                if f:
                    flag[i]=False
                    fun(n+1,tmp+[nums[i]])
                    flag[i]=True
        fun(0,[])
        return ans