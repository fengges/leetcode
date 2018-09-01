class Solution:
    def exclusiveTime(self, n, logs):
        dic={i:0 for i in range(n)}
        sum={i:0 for i in range(n)}
        list=[]
        for l in logs:
            w=l.split(":")
            if w[1]=="start":
                list.append(w)
            else:
                temp=list[-1]
                del list[-1]
                t=int(w[2])-int(temp[2])+1

                dic[int(w[0])]+=t-sum[int(w[0])]
                sum[int(w[0])] = 0
                if len(list)>0:
                    sum[int(list[-1][0])]+=t
        return [dic[k] for k in dic]


s=Solution()
test=[
{"input":[2,["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]], "output":[7,1]},
{"input":[2,["0:start:0",
 "1:start:2",
 "1:end:5",
 "0:end:6"]], "output":[3, 4]},
]

for t in test:
    r=s.exclusiveTime(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.exclusiveTime(t['input'][0],t['input'][1])
