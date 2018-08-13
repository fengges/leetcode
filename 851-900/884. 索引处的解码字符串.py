class Solution:
    def decodeAtIndex(self, S, K):
        index=0
        dic={}
        for i in S:
            if i>="0" and i<="9":
                for d in dic:
                    item=[]
                    for t in dic[d]:
                        for l in range(1,int(i)):
                            tmp=t+index*l
                            if tmp==K:
                                return d
                            item.append(tmp)
                    dic[d].extend(item)
                index = index * int(i)
            else:
                index = index +1
                if i in dic:
                    dic[i].append(index)
                else:
                    dic[i]=[index]
                if index==K:
                    return i

s=Solution()
test=[
{"input":["y959q969u3hb22odq595",222280369], "output":"1"},
{"input":["leet2code3",10], "output":"o"},
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
