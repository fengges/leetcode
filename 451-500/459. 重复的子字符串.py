class Solution:
    def repeatedSubstringPattern(self, s):
        size=len(s)
        if size<=1:
            return False
        for i in range(2,size+1):
            if size%i==0:
                length=int(size/i)
                for j in range(length):
                    for k in range(i-1):
                        if s[j+k*length]!=s[j+(k+1)*length]:
                            break
                    else:
                        continue
                    break
                else:
                    return True
        return False
s=Solution()
test=[
{"input":"bbb", "output":True},
{"input":"abac", "output": False},
{"input":"aba", "output": False},
{"input":"abab", "output": True},
{"input":"abcabcabcabd", "output": True},
]

for t in test:
    r=s.repeatedSubstringPattern(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
