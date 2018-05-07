import time
class Solution:
    def threeSumClosest(self, nums, target):

        nums.sort()
        if len(nums)>=3:
            temp=nums[0:3]
            for  n in range(3,len(nums)):
                if nums[n-3]!=nums[n]:
                    temp.append(nums[n])
            nums=temp
        lenn = len(nums)
        min=10000000
        mixsum=0
        for i in range(1,lenn-1):
            left=i-1
            right=i+1
            while left>=0 and right<lenn:
                sum=nums[i]+nums[left]+nums[right]
                if sum>target:
                    gap=sum-target
                    if gap<min:
                        min=gap
                        mixsum=sum
                    left-=1
                elif sum<target:
                    gap=target-sum
                    if gap<min:
                        min = gap
                        mixsum = sum
                    right+=1
                else:
                    return target
        return mixsum

s=Solution()

test=[
{"input": [[-1,2,1,-4],1],"output":2},
{"input": [[0,0,0],1],"output":0},


      ]

for t in test:
    r=s.threeSumClosest(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.threeSumClosest(t['input'][0],t['input'][1])