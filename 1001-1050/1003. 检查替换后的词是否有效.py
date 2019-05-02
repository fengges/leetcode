class Solution:
    def isValid(self, S):
        stack=[]
        for s in S:
            if s=="c":
                if len(stack)>=2 and stack[-1]=='b' and stack[-2]=='a':
                    stack.pop()
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s)
        return len(stack)==0
