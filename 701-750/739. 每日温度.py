class Solution:
    def dailyTemperatures(self, T):
        stack=[]
        r=[0 for i in range(len(T))]
        for i,v in enumerate(T):
            while len(stack)!=0 and stack[-1][0] < v:
                tmp=stack.pop()
                r[tmp[1]] = i - tmp[1]
            stack.append([v, i])
        return r
s = Solution()
test = [
{"input":  [73, 74, 75, 71, 69, 72, 76, 73], "output":[1, 1, 4, 2, 1, 1, 0, 0]},
{"input": [89,62,70,58,47,47,46,76,100,70], "output":[1, 1, 4, 2, 1, 1, 0, 0]},

]

for t in test:
    r = s.dailyTemperatures(t['input'])
    if r != t['output']:
        print("error:" + str(t) + " out:" + str(r))
