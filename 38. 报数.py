class Solution:
    def countAndSay(self, n):
        result=['1']
        while n>len(result):
            temp=str(result[-1])
            s=temp[0]
            num=0
            next=''
            for t in temp:
                if t==s:
                    num+=1
                else:
                    next+=str(num)+s
                    s=t
                    num=1
            next += str(num) + s
            result.append(next)
        return result[-1]

s=Solution()

test=[
{"input":1,"output":'1'},
{"input":4,"output":"1211"},
      ]

for t in test:
    r=s.countAndSay(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.countAndSay(t['input'])