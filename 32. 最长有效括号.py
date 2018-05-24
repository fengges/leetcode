
class Solution:
    def longestValidParentheses2(self, s):
        max=0
        index=[ False for t in s]
        while True:
            left=-1
            right=-1
            for i in range(len(s)):
                if s[i]=="(" and not index[i]:
                    left=i
                elif s[i]==")" and not index[i] and left>=0:
                    right=i
                    break
            if right==-1:
                break
            else:
                index[left]=True
                index[right]=True
        num=0
        for i in index:
            if i:
                num+=1
                if num>max:
                    max=num
            else:
                num=0
        return max
    def longestValidParentheses(self, s):
        max=0
        left=0
        num=0
        for t in s:
            if t=='(':
                left+=1
            else:
                left-=1
                if left>=0:
                    num+=2
                else:
                    if num>max:
                        max=num
                    num=0
                    left=0
        if num > max:
            max = num
        return max

s=Solution()

test=[
{"input":"()(()","output":2},
{"input":"()","output":2},
{"input":")(((((()())()()))()(()))(","output":22},
{"input":"(()","output":2},
{"input":")()())","output":4},
      ]

for t in test:
    r=s.longestValidParentheses(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.longestValidParentheses(t['input'])