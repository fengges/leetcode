
class Solution:
    def findIndex(self,nums):
        i=0
        j=0
        for j in range(len(nums)-2,-1,-1):
            temp=nums[j+1:]
            min=100000000000000
            for t in temp:
                if t>nums[j] and t<min:
                    min=t
            try:
                i=temp.index(min)
            except:
                i=-1
            if i>=0:
                i+=j+1
                return [i,j]
        return []
    def nextPermutation(self, nums):

        index=self.findIndex(nums)
        if len(index)==2:
            i, j = index[0], index[1]
            nums[i],nums[j]=nums[j],nums[i]
            temp=nums[j+1:]
            temp.sort()
            for t in range(len(temp)):
                nums[j+t+1]=temp[t]
        else:
            nums.sort()
        return nums
s=Solution()

test=[
{"input":[5,4,7,5,3,2],"output":[5,5,2,3,4,7]},
{"input":[4,2,0,2,3,2,0],"output":[4,2,0,3,0,2,2]},
{"input":[1,3,2],"output":[2,1,3]},
{"input": [1,2,3],"output":[1,3,2]},
{"input":[3,2,1],"output":[1,2,3]},
{"input":[1,1,5],"output":[1,5,1]},
      ]

for t in test:
    r=s.nextPermutation(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.nextPermutation(t['input'])

