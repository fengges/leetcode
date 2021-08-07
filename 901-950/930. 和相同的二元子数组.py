class Solution:
    def numSubarraysWithSum(self, A, S):
        s,e,size=0,0,len(A)
        r,sum=0,0
        while s<=size or e<=size:
            if sum==S and s<e:
                r+=1
                if e==size:
                    sum -= A[s]
                    s+=1
                else:
                    sum += A[e]
                    e+=1
            elif sum<=S:
                if sum==S and s<e:
                    r+=1
                if e==size:
                    break
                else:
                    sum += A[e]
                    e+=1


            else:
                sum-=A[s]
                s+=1
        return r
s=Solution()
test=[
{"input":  [[0,0,0,0,0],0],"output":15},
{"input":  [[1,0,1,0,1],2],"output":4},
]

for t in test:
    r=s.numSubarraysWithSum(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))