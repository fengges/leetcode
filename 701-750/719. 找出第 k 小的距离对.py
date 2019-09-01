class Solution:
    def smallestDistancePair(self, nums, k):
        size=len(nums)
        ans={}
        for i in range(size):
            ans[nums[i]]=ans.get(nums[i],0)+1
        dict={}
        dict[0]=int(sum([0.5*ans[k]*(ans[k]-1) for k in ans]))
        key=[ k for k in ans]
        size1=len(key)
        for i in range(size1):
            for j in range(i+1,size1):
                t=abs(key[i]-key[j])
                dict[t]=dict.get(t,0)+ans[key[i]]*ans[key[j]]
        tmp=sorted(dict.items(),key=lambda x:x[0])
        for t in tmp:
            if k<=t[1]:
                return t[0]
            else:
                k-=t[1]

s=Solution()
test=[
{"input": [[9,10,7,10,6,1,5,4,9,8],18], "output":2},
{"input": [[1,6,1],3], "output":5},
{"input": [[1,3,1],1], "output":0},

]

for t in test:
    r=s.smallestDistancePair(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
