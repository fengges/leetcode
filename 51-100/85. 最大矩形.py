class Solution:
    def maximalRectangle(self, matrix):
        r=0
        if len(matrix)==0:
            return r
        heights=[0 for i in range(len(matrix[0]))]
        for line in matrix:
            for i,v in enumerate(line):
                if v=="0":
                    heights[i]=0
                else:
                    heights[i] +=1
            r=max(r,self.largestRectangleArea(heights))
        return r
    def largestRectangleArea(self, heights):
        res = 0
        st=[]
        heights.append(0)
        i=0
        while i<len(heights):
            if len(st)==0 or heights[st[-1]] < heights[i]:
               st.append(i)
               i+=1
            else:
               cur = st[-1]
               del st[-1]
               if len(st)==0:
                   length=i
               else:
                   length=i - st[-1] - 1
               res = max(res, heights[cur] * length)
        return res

s=Solution()
test=[
{"input": [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]], "output": 6},
]

for t in test:
    r=s.maximalRectangle(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.maximalRectangle(t['input'])