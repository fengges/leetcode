
class Solution:

    def longestValidParentheses(self, s):
        index=[{"s":t,"is":False} for t in s]
        stack=[]
        for i in range(len(index)):
            if index[i]["s"]=="(":
                stack.append(index[i])
            else:
                if len(stack)!=0:
                    index[i]["is"]=True
                    stack[-1]['is']=True
                    del stack[-1]

        max=0
        temp=0
        for i in range(len(index)):
            if index[i]["is"]:
                temp+=1
                if temp>max:
                    max=temp
            else:
                temp=0

        return max

s=Solution()

test=[
{"input":"()(()","output":2},
{"input":")()())","output":4},
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