class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        size,s=len(rolls),sum(rolls)
        avg=(mean*(size+n)-s)/n
        if avg>6 or avg<1 :
            return []
        tmp=[int(avg) for i in range(n)]
        l=int(mean*(size+n)-s-sum(tmp))
        # if n==87141:
        #     print(avg,l,s,sum(tmp))
        for i in range(l):
            tmp[i]+=1

        return tmp
