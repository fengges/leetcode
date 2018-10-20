class Solution:
    def numFriendRequests(self, ages):
        dic={}
        for i in ages:
            if i not in dic:
                dic[i]=0
            dic[i]+=1
        ages=[k for k in dic]
        ages.sort(reverse=True)
        r=0
        for i in range(len(ages)):
            for j in range(i,len(ages)):
                if ages[i]==ages[j] and (ages[j] > 0.5 * ages[i] + 7) and not(ages[j] > 100 and ages[i] < 100):
                    r+=dic[ages[i]]*(dic[ages[i]]-1)
                elif  (ages[j] <= 0.5 * ages[i] + 7) or(ages[j] > 100 and ages[i] < 100):
                    continue
                else:
                    r+=dic[ages[i]]*dic[ages[j]]
        return r

s=Solution()
test=[
{"input":  [16,16], "output":2},
{"input":  [16,17,18], "output":2},
{"input":  [49,110,13,39,45,104,9,114,86,72,13,24,10,77,103,85,9,21,66,25], "output":47},
]

for t in test:
    r=s.numFriendRequests(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))

