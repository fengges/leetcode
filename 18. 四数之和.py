
class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        if len(nums) >= 4:
            temp = nums[0:4]
            for n in range(4, len(nums)):
                if nums[n - 4] != nums[n]:
                    temp.append(nums[n])
            nums = temp
        lenn = len(nums)
        min = 10000000
        mixsum = 0
        r=[]
        dic={}
        for i in range(0, lenn - 3):
            for j in range(i+1,lenn-2):
                left = j + 1
                right = lenn-1
                while left<right:
                    sum = nums[i] + nums[j]+ nums[left] + nums[right]
                    if sum > target:
                        right -= 1
                    elif sum < target:
                        left += 1
                    else:
                        s=str(nums[i]) +','+ str(nums[j])+ ','+str(nums[left]) +','+ str(nums[right])
                        if s in dic:
                            pass
                        else:
                            dic[s]=1
                            r.append([ nums[i],nums[j], nums[left] , nums[right]])
                        left+=1
        return r

s=Solution()

test=[
{"input": [[-3,-2,-1,0,0,1,2,3],1],"output":[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]},
{"input": [[1, 0, -1, 0, -2, 2],0],"output":[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]},
      ]

for t in test:
    r=s.fourSum(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.fourSum(t['input'][0],t['input'][1])