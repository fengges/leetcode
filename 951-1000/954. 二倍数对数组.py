import collections
class Solution:

    def canReorderDoubled(self, A):
        count = collections.Counter(A)
        for x in sorted(A, key = abs):
            if count[x] == 0: continue
            if count[2*x] == 0: return False
            count[x] -= 1
            count[2*x] -= 1

        return True

s=Solution()
null=None
test=[
    {"input":[1,2,1,-8,8,-4,4,-4,2,-2],"output": True},
    {"input":[-5,-3],"output": False},
    {"input":[4,-2,2,-4],"output": True},

]
for t in test:
    r=s.canReorderDoubled(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
