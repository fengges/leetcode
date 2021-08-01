class Solution:
    def sumOddLengthSubarrays(self, arr):
        size=len(arr)
        t=(size+1)//2
        tmp=[t for a in arr]

        for i in range(3,size,2):
            index=i//2
            tmp[index]=tmp[index-1]+1
            tmp[size-1-index]=tmp[index-1]+1
        print(tmp)
        return 1

s=Solution()
null=None
test=[
{"input": [1,4,2,5,3],"output":58},
{"input": [1,2],"output":3},
{"input":[10,11,12],"output":66},
]
for t in test:
    r=s.sumOddLengthSubarrays(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))