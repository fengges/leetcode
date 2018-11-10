class Solution(object):
    def minAddToMakeValid(self, S):
        stack=[]
        r=0
        for s in S:
            if s=="(":
                stack.append(s)
            else:
                if len(stack)==0:
                    r+=1
                else:
                    del stack[-1]
        r+=len(stack)
        return r