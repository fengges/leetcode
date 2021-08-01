class Solution:
    def decode(self, encoded, first) :
        ans=[first]
        for e in encoded:
            ans.append(ans[-1]^e)
        return ans
