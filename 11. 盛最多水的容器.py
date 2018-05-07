class Solution:
    def maxArea(self, height):
        maxA=0
        left=0
        right=len(height)-1
        while left<right:
            if height[left]<=height[right]:
                isLeft=True
                minh=height[left]
            else:
                isLeft=False
                minh = height[right]
            area=minh*(right-left)
            if area>maxA:
                maxA=area
            if isLeft:
                left+=1
            else:
                right-=1
        return maxA


s=Solution()

test=[
{"input":[2,1],"output":1},
{"input":[1,1],"output":1},
      ]

for t in test:
    r=s.maxArea(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.maxArea(t['input'])