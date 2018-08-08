class Solution:
    def maximumSwap(self, num):
        num_str=str(num)
        r_num=[n for n in num_str]
        r_num.sort()
        r_num.reverse()
        num_str=[n for n in num_str]
        for index,value in enumerate(num_str):
            if value!=r_num[index]:
                p=''.join(num_str[index:]).rfind(r_num[index])+index
                tmp=num_str[p]
                num_str[p]=num_str[index]
                num_str[index]=tmp
                return int(''.join(num_str))
        return num
s = Solution()
test = [
    {"input": 2736, "output": 7236},
    {"input": 1993, "output":9913},

]

for t in test:
    r = s.maximumSwap(t['input'])
    if r != t['output']:
        print("error:" + str(t) + " out:" + str(r))
        r = s.maximumSwap(t['input'])