class Solution(object):
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        m=S.count('0')   #分界点为0之前，统计之后的0
        res=[m]
        for x in S:
            if x=='1':   #如果是1，分界点之前1的个数+1，分界点之后0的个数不变
                m+=1
            else:       #如果是0，分界点之前1的个数不变，分界点之后0的个数减1
                m-=1
            res.append(m)
        return min(res)