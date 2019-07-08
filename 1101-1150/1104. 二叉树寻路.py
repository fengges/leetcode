class Solution:
    def pathInZigZagTree(self, label):
        res = []
        while label != 1:
            res.append(label)
            label >>= 1
            # 这里我采用异或实现
            label = label ^(1 << (label.bit_length() - 1)) - 1
        return [1]+res[::-1]
s=Solution()
test=[
{"input":26 , "output":[1,2,6,10,26]},
]
for t in test:
    r=s.pathInZigZagTree(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))