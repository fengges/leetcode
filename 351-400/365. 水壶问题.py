class Solution:
    def canMeasureWater(self, x, y, z ):
        global hcf
        if x + y < z:
            return False
        smaller = min(x, y)
        for i in range(1, smaller+1):
            if x % i == 0 and y % i == 0:
                hcf = i  # 存在更大的值时会覆盖原来的hcf，最后剩下最大公约数
        if z % hcf == 0:
            return True
        return False


s=Solution()

test=[
{"input": [22003,31237,1],"output": True},
{"input": [3,5,4],"output": True},

]
for t in test:
    r=s.canMeasureWater(t['input'][0],t['input'][1],t['input'][2])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))