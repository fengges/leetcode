class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s)<=2:
            return s
        stack=[s[0],s[1]]
        for a in s[2:]:
            if stack[-1]==a:
                if  stack[-2]!=a:
                    stack.append(a)
                else:
                    continue
            else:
                stack.append(a)
        return ''.join(stack)


