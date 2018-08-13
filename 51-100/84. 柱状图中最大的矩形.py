class Solution:
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
{"input": [2,1,5,6,2,3], "output": 10},
]

for t in test:
    r=s.largestRectangleArea(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.largestRectangleArea(t['input'])