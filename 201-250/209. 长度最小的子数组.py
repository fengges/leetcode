class Solution:
    def minSubArrayLen(self, s, nums):
        start,end,r,tmp,size=0,0,len(nums)+1,0,len(nums)
        while True:
            if end>=size and start>=size:
                break
            if tmp>=s:
                if start==end:
                    if end<size:
                        tmp += nums[end]
                        end += 1
                    continue
                r=min(r,end-start)
                tmp-=nums[start]
                start+=1
            else:
                if end==size:
                    if start<end:
                        tmp -= nums[start]
                        start += 1
                    continue
                tmp+=nums[end]
                end+=1
        if r==size+1:
            return 0
        return r

s=Solution()
test=[
{"input":[7, [2,3,1,2,4,3]], "output":2},

]
for t in test:
    r=s.minSubArrayLen(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))

