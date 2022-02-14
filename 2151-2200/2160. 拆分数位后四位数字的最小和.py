class Solution:
    def minimumSum(self, num: int) -> int:
        tmp=[int(a) for a in str(num)]
        tmp.sort()
        return (tmp[0]+tmp[1])*10+tmp[2]+tmp[3]