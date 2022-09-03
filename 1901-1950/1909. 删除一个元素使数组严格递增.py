class Solution:
    def canBeIncreasing(self, nums) -> bool:

        flag=[True for n in nums]
        self.ans=[]
        def dps(index,r):
            if index>=len(flag):
                return

            if len(self.ans)>(len(r)+len(flag)-1-index):
                return
            if r[-1]<nums[index]:
                self.ans=max(self.ans,r+[nums[index]],key=len)
                dps(index+1,r+[nums[index]])

            dps(index+1,r)

        dps(0,[float('-inf')])
        return len(flag)-(len(self.ans)-1)<=1

s=Solution()

test=[
    {"input":[1,2,10,5,7],"output":3},


]
for t in test:
    r=s.canBeIncreasing(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))