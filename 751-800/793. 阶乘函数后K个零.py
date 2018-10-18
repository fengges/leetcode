class Solution(object):
    def calcFactorial(self,v):
        n = v
        count = 0
        while n > 0:
            t=int(n/5)
            count +=t
            n = t
        return count

    def preimageSizeFZF(self, K):
        high = K*5
        low = 0
        while low <= high:
            mid = int((high + low)/2)
            if self.calcFactorial(mid) < K:
                low = mid +1
            elif self.calcFactorial(mid) > K:
                high = mid - 1
            else:
                return 5
        return 0

s=Solution()
test=[
{"input": 3, "output":5},
{"input": 5, "output":0},
{"input": 0, "output":5},
{"input":80502705, "output":5},


]

for t in test:
    r=s.preimageSizeFZF(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
