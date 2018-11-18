class Solution(object):
    def scoreOfParentheses(self, S):
        char_stack=[]
        num_stack=[]
        for i in range(len(S)-1):
            t=S[i:i+2]
            if t=="((":
                char_stack.append('*')
            elif t=="()":
                num_stack.append(1)
            elif t==")(":
                char_stack.append('+')
            else:
                while True:
                    if char_stack[-1]=="*":
                        del char_stack[-1]
                        num_stack[-1]=2*num_stack[-1]
                        break
                    else:
                        num_stack[-2]=num_stack[-1]+num_stack[-2]
                        del num_stack[-1]
                        del char_stack[-1]
        while len(char_stack)!=0:
            num_stack[-2] = num_stack[-1] + num_stack[-2]
            del num_stack[-1]
            del char_stack[-1]
        return num_stack[0]

s = Solution()
test = [
{"input": "()()()","output":3},
{"input": "(()(()))","output":6},
{"input": "()()", "output": 2},
]

for t in test:
    r = s.scoreOfParentheses(t['input'])
    if r != t['output']:
        print("error:" + str(t) + " out:" + str(r))