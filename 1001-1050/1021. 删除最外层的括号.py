class Solution:
    def removeOuterParentheses(self, S):
        stack=[]
        r=""
        for s in S:
            if s=="(":
                if len(stack) != 0:
                    r += s
                stack.append("(")
            else:
                stack.pop()
                if len(stack)!=0:
                    r += s
        return r
s=Solution()

test=[
{"input":"(()())(())","output":"()()()"},
{"input":"(()())(())(()(()))","output":"()()()()(())"},
{"input":"()()","output":""},
]
for t in test:
    r=s.removeOuterParentheses(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
