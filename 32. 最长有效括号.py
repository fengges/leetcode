
class Solution:

    def longestValidParentheses(self, s):
        max=0
        temps=s
        index=0
        t=0
        while True:
            temp=s[t:].find('()')
            if temp<0:
                break

        return max

s=Solution()

test=[
{"input":")(((((()())()()))()(()))(","output":22},
{"input":"(()","output":2},
{"input":")()())","output":4},
      ]

for t in test:
    r=s.longestValidParentheses(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.longestValidParentheses(t['input'])