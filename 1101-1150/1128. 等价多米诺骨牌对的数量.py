class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        dicts=[]
        ans=0
        for d in dominoes:
            a,b=min(a),max(b)
            v=a*10+b
            ans+=dicts.get(v,0)
            dicts[v]=dicts.get(v,0)+1
        return ans