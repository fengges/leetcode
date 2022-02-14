import time
class Solution:
    def threeSum(self, nums):
        # st=time.time()

        r=[]
        dic={}
        nums.sort()
        if len(nums)>=3:
            temp=nums[0:3]
            for  n in range(3,len(nums)):
                if nums[n-3]!=nums[n]:
                    temp.append(nums[n])
            nums=temp
        lenn = len(nums)
        for i in range(1,lenn-1):
            left=i-1
            right=i+1
            while left>=0 and right<lenn:
                if nums[i]+nums[left]+nums[right]>0:
                    left-=1
                elif nums[i]+nums[left]+nums[right]<0:
                    right+=1
                else:
                    s=str(nums[left])+','+str(nums[i])+','+str(nums[right])
                    t=[nums[left],nums[i],nums[right]]
                    dic[s]=t
                    left-=1
        for k in dic:
            r.append(dic[k])
        # print(time.time()-st)
        return r