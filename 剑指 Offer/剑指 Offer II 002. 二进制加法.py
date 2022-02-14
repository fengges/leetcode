class Solution:
    def addBinary(self, a, b):
        lena,lenb=len(a),len(b)
        maxL=max(lena,lenb)
        numa=[ int(s) for s in a]
        numb = [int(s) for s in b]
        numa.reverse()
        numb.reverse()
        numa.extend([0 for i in range(maxL-lena)])
        numb.extend([0 for i in range(maxL - lenb)])
        isJin=0
        result=[0 for i in range(maxL)]
        for i in range(maxL):
            r=numa[i]+numb[i]+isJin
            if r>=2:
                result[i]=r-2
                isJin=1
            else:
                result[i]=r
                isJin=0

        if isJin==1:
            result.append(1)
        result.reverse()
        result=[str(r) for r in result]
        return "".join(result)

