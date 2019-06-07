class Solution:
    def isLongPressedName(self, name, typed):
        start = 0
        for i in range(len(typed)):
            if start<len(name) and typed[i] == name[start]:
                start += 1
            else:
                if start == 0:
                    return False
                elif typed[i] != name[start - 1]:
                    return False
        return start==len(name)
s=Solution()
test=[
{"input":["pyplrz","ppyypllr"], "output":False},
]
for t in test:
    r=s.isLongPressedName(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
