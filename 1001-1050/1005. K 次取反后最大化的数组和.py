class Solution:
    def largestSumAfterKNegations(self, A, K):
        fu=[i for i in A if i<0 ]
        fu.sort()
        zheng=[i for i in A if i>=0 ]
        zheng.sort()
        if len(fu)>=K:
            for i in range(K):
                fu[i]=-fu[i]
            zheng.extend(fu)
        else:
            left=K-len(fu)
            fu = [-n for n in fu]
            zheng.extend(fu)
            zheng.sort()
            if left%2!=0:
                zheng[0]=-zheng[0]
        return sum(zheng)
