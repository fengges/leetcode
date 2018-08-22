class Solution:
    def rotate(self, nums, k):
        k=k%len(nums)
        self.reverse(nums,0,len(nums)-k)
        self.reverse(nums, len(nums) - k,len(nums))
        self.reverse(nums, 0, len(nums))
    def reverse(self,nums,s,e):
        for i in range(s,int((s+e)/2)):
            nums[i],nums[s+e-i-1]=nums[s+e-i-1],nums[i]

s=Solution()

test=[
{"input":[[1,2,3,4,5,6,7],3],"output": 7},
]
for t in test:
    r=s.rotate(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))

