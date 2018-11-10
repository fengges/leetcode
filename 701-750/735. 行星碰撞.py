class Solution(object):
    def asteroidCollision(self, asteroids):
        stack=[]
        for i in asteroids:
            while len(stack)>0 and stack[-1]>0 and i<0 and -i>stack[-1]:
                del stack[-1]
            if len(stack)==0:
                stack.append(i)
            elif stack[-1]>0 and i<0:
                if stack[-1]+i==0:
                    del stack[-1]
            else:
                stack.append(i)
        return stack
s = Solution()
test = [
    {"input": [5,10,-5],"output":[5,10]},
    {"input": [8, -8], "output": []},
    {"input": [10, 2, -5], "output":[10]},
    {"input":  [-2, -1, 1, 2], "output": [-2, -1, 1, 2]},
]

for t in test:
    r = s.asteroidCollision(t['input'])
    if r != t['output']:
        print("error:" + str(t) + " out:" + str(r))