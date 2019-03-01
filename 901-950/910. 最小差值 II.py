class Solution:
    def smallestRangeII(self, A, K):
        tmp=max(A)-min(A)
        avg=1.0*sum(A)/len(A)
        for i in range(len(A)):
            if avg>A[i]:
                A[i]+=K
            elif avg==A[i]:
                print(A)
                print(K)
            else:
                A[i]-=K

        return min(max(A)-min(A),tmp)

s=Solution()

test=[
{"input":[[7,8,8,5,2],4],"output":1},
{"input":[[7,8,8],5],"output":1},
{"input":[[1,3,6],3],"output":3},
{"input":[[0,10],2],"output":6},

]
for t in test:
    r=s.smallestRangeII(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))