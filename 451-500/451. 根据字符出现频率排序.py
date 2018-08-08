class Solution:
    def frequencySort(self, s):
        dic={}
        for n in s:
            if n not in dic:
                dic[n]=0
            dic[n]+=1
        res=sorted(dic.items(), key=lambda x: x[1], reverse=True)
        str=""
        for r in res:
            str+=r[0]*r[1]
        return str
