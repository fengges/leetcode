class Solution:
    def decodeString(self, s):
        stack=[]
        for i in s:
            if i=="]":
                tmp=""
                while stack[-1]!="[":
                    tmp=stack[-1]+tmp
                    stack.pop()
                stack.pop()
                num=int(stack[-1])
                tmp=tmp*num
                stack.pop()
                stack.append(tmp)
            elif i.isdigit() and (len(stack)>0 and stack[-1].isdigit()):
                stack[-1]=stack[-1]+i
            else:
                stack.append(i)
        return ''.join(stack)

s=Solution()
test=[
{"input": "100[leetcode]", "output":"aaabcbc"},
{"input": "3[a]2[bc]", "output":"aaabcbc"},
{"input": "3[a2[c]]", "output":"accaccacc"},
{"input":"2[abc]3[cd]ef", "output":"abcabccdcdcdef"},
]

for t in test:
    r=s.decodeString(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
