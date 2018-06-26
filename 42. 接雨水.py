class Solution:
    def trap(self, height):
        ret = 0
        if len(height) == 0:
            return ret;
        lmax ,rmax = 0,0
        l , r = 0,len(height) - 1;
        while l < r:

            lmax = max(lmax, height[l])
            rmax = max(rmax, height[r])
            if lmax < rmax:
                ret += lmax-height[l]
                l+=1
            else:
                ret += rmax-height[r]
                r-=1
        return ret


s=Solution()

test=[
{"input":[5,4,1,2],"output":1},
{"input":[0,1,0,2,1,0,1,3,2,1,2,1],"output":6},
{"input":[5,2,1,2,1,5],"output":14},
      ]

for t in test:
    r=s.trap(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.trap(t['input'])
