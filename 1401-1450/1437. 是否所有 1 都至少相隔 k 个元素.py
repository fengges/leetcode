class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        t=''.join([str(n) for n in nums]).split('1')
        if len(t)<=2:return True
        t.pop()
        t.pop(0)
        # if not t: return True
        # print(t,[len(a) for a in t])
        return min([len(a) for a in t])>=k