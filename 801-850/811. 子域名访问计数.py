class Solution(object):
    def subdomainVisits(self, cpdomains):
        dic={}
        for i in cpdomains:
            tmp=i.split(' ')
            path=tmp[1].split('.')
            num=int(tmp[0])
            for j in range(len(path)):
                p='.'.join(path[j:])
                if p not in dic:
                    dic[p]=0
                dic[p]+=num
        return [str(dic[k])+" "+k for k in dic]
