class Solution:
    def findCircleNum(self,M):
        group=len(M)
        pre=[i for i in range(group)]
        size=group
        for i in range(size):
            for j in range(size):
                if i != j and M[i][j] == 1:
                    x1 = find(i, pre)
                    x2 = find(j, pre)
                    if (x1 != x2):
                        pre[x1] = x2
                        group-=1
        return group

    def find(self,x,  pre):
        if pre[x] == x :
            return x
        else:
            pre[x] = find(pre[x], pre)
            return pre[x]
