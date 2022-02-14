class Solution:
    def luckyNumbers (self, matrix) :
        a=[min(m) for m in matrix]
        size=len(matrix)
        b=[max([matrix[j][i] for j in range(size)])  for i in range(len(matrix[0]))]

        ans=[]
        for i,mat in enumerate(matrix):
            for j,m in enumerate(mat):
                if m==a[i] and m==b[j]:
                    ans.append(m)
        return ans

s=Solution()

test=[
    {"input":[[1,10,4,2],[9,3,8,7],[15,16,17,12]],"output":[7]},


]


for t in test:
    r=s.luckyNumbers(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))