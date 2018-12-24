class Solution:
    def cmp(self,a, b,sort):
        if len(a) == 0 and len(b) == 0:
            return True
        elif len(a) == 0:
            return True
        elif len(b) == 0:
            return False
        else:
            t = sort[a[0]] - sort[b[0]]
            if t == 0:
                return self.cmp(a[1:], b[1:],sort)
            else:
                return t<0
    def isAlienSorted(self, words, order):
        dic={v:i for i,v in enumerate(order)}
        for i in range(1,len(words)):
            if self.cmp(words[i-1],words[i],dic):
                continue
            else:
                return False
        return True



s=Solution()
test=[
{"input":  [["hello","leetcode"],"hlabcdefgijkmnopqrstuvwxyz"],"output":12},
]

for t in test:
    r=s.isAlienSorted(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))