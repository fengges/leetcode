class Solution:
    def isMatch(self, s, p):
        lenp=len(p)
        lens=len(s)
        next_p=0
        next_s = 0
        while next_s<lens and next_p<lenp:
            a=s[next_s]
            if a!=p[next_p] and p[next_p]!='.':
                if (next_p + 1) < lenp and p[next_p + 1] == '*':
                    next_p += 2
                    continue
                else:
                    return False
            if (next_p+1)<lenp and p[next_p+1]=='*':
                pass
            else:
                next_p += 1
            next_s+=1
        t=next_p
        ish=False
        while next_p<lenp:
            if next_p+1<lenp and p[next_p+1]=='*':
                ish=True
                next_p+=2
            else:
                if (p[t]==p[next_p] or p[t]=='.') and ish:
                    next_p+=1
                break
        if next_s<lens:
            return False
        elif next_p==lenp :
            return True
        else:
            return False


s=Solution()
test=[
{"input": ("bbbba",".*a*a"), "output": True},
{"input": ("aab", "c*a*b"), "output": True},
{"input": ("aaa","aaaa"), "output": False},
{"input": ("aaa","ab*a*c*a"), "output": True},
{"input": ("aaa","a*a"), "output": True},
{"input": ("aa", "a"), "output": False},
{"input": ("aa", "a*"), "output":True},
{"input": ("ab",".*"), "output": True},

{"input":("mississippi","mis*is*p*."),"output":False},
      ]

for t in test:
    r=s.isMatch(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.isMatch(t['input'][0], t['input'][1])