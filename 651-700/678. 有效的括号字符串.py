class Solution:
    def checkValidString(self, s: str) -> bool:
        def fun(tmp,val):
            if tmp=='':
                return val==0
            if tmp[0]=='(':
                return fun(tmp[1:],val+1)
            elif tmp[0]==')':
                return False if val<=0 else fun(tmp[1:],val-1)
            else:
                return fun(tmp[1:],val+1) or fun(tmp[1:],val) or (val>0 and fun(tmp[1:],val-1))

        return fun(s,0)

s = Solution()
test = [
    {"input": "(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())", "output": True},


]

for t in test:
    r = s.checkValidString(t['input'])
    if r != t['output']:
        print("error:" + str(t) + " out:" + str(r))
