class Solution:
    def numSubarraysWithSum(self, A, S):
        sum = 0
        cnt={}
        ret = 0
        for num in A:
            cnt[sum]=cnt.get(sum,0)+1
            sum += num;
            ret += cnt.get(sum-S,0);

        return ret


s=Solution()
test=[
{"input":  [[0,0,0,0,0],0],"output":15},
{"input":  [[1,0,1,0,1],2],"output":4},
]

for t in test:
    r=s.numSubarraysWithSum(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))