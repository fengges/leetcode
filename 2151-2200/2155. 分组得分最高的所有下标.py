class Solution:
    def maxScoreIndices(self, nums ) :
        size,suma=len(nums),sum(nums)

        ans,index=suma,0
        result=[0]
        for i,n in enumerate(nums):
            if n==1:
                index+=1
            tmp=i+suma-2*index+1
            if ans<tmp:
                result=[i+1]
                ans=tmp
            elif ans==tmp:
                result.append(i+1)
        return result

s=Solution()

test=[
    {"input": [0,0,1,0],"output":[2,4]},

]
for t in test:
    r=s.maxScoreIndices(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))