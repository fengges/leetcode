class Solution:
    def decodeAtIndex(self, S, K):
        num=0
        index=0
        for index,i in enumerate(S):
            if i>="0" and i<="9":
                num=num*int(i)
            else:
                num+=1
            if num>=K:
                break
        i=0
        for i in range(index,-1,-1):
            if S[i]>="0" and S[i]<="9":
                num=int(num/int(S[i]))
                K=K%num
            else:
                if K%num==0:
                    return S[i]
                num-=1


s=Solution()
test=[

{"input":["leet2code3",10], "output":"o"},
{"input":["y959q969u3hb22odq595",222280369], "output":"1"},
{"input":["a23",6], "output":"a"},
{"input":["a2b3c4d5e6f7g8h9",3], "output":"b"},

{"input":["ha22",5], "output":"h"},
{"input":["a2345678999999999999999",1], "output":"a"},
]

for t in test:
    r=s.decodeAtIndex(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.decodeAtIndex(t['input'][0], t['input'][1])
