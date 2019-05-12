class Solution:
    def findLengthOfLIS2(self,nums,num,start,length):
        if start==len(nums):
            return length
        len1=self.findLengthOfLIS2(nums,num,start+1,length)
        if nums[start]>num:
            len2=self.findLengthOfLIS2(nums,nums[start],start+1,length+1)
            return max(len1,len2)
        else:
            return len1

    def findNumberOfLIS(self,nums):
        self.findLengthOfLIS2(nums)
    def findNumberOfLIS2(self, nums):
        size = len(nums)
        res = [[1,1] for n in nums]
        for i in range(1, size):
            for j in range(i):
                if nums[j] < nums[i]:
                    if res[j][0] + 1>res[i][0]:
                        res[i]=[res[j][0] + 1,res[j][1]]
                    elif res[j][0] + 1==res[i][0]:
                        res[i][1] +=res[j][1]
        index=None
        t=0
        for r in range(len(res)):
            if index is None:
                index = r
                t=res[r][1]
            elif res[r][0]>res[index][0]:
                index=r
                t = res[r][1]
            elif res[r][0]==res[index][0]:
                t+= res[r][1]
        return t

s=Solution()

test=[
{"input":[1,3,6,5,7],"output":27},
{"input":[1,1,1,2,2,2,3,3,3],"output":27},
{"input":[1,2,4,3,5,4,7,2],"output":3},
{"input":[2,2,2,2,2],"output": 5},

]
for t in test:
    r=s.findNumberOfLIS(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))