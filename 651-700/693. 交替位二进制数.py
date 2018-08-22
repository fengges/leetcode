class Solution(object):
    def hasAlternatingBits(self, n):
        t=self.get(n)
        for i in range(len(t)-1):
            if t[i+1]==t[i]:
                return False
        return True
    def get(self,n):
        tmp=["0" for i in range(32)]
        for i in range(32):
            if n&1==1:
                tmp[i]="1"
            n=n>>1
        tmp.reverse()
        s="".join(tmp).lstrip('0')
        return s

s = Solution()
test = [
{"input":5, "output": 3},

]

for t in test:
    r = s.hasAlternatingBits(t['input'])
    if r != t['output']:
        print("error:" + str(t) + " out:" + str(r))
        r = s.hasAlternatingBits(t['input'])