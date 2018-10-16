class Solution:
    def originalDigits(self, s):
        dic = {}
        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        tmp = []
        num = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        num_dic = []
        for n in num:
            t = {i: 0 for i in n}
            for i in n:
                t[i] += 1
            num_dic.append(t)
        seq = [{'z': 0},{'w': 2},{'u': 4},{'x': 6},{'g': 8},{'t': 3},{'o': 1},{ 'f': 5},{ 'v': 7},{'i': 9}]
        for s in seq:
            se=list(s.keys())[0]
            if se not in dic:
                continue
            lens = dic[se]
            if lens == 0:
                continue
            n = s[se]
            t_dic = num_dic[n]
            for k in t_dic:
                dic[k] -= t_dic[k] * lens
            print(dic)
            tmp.extend([n for i in range(lens)])
        tmp.sort()
        return ''.join([str(t) for t in tmp])

s=Solution()

test=[
{"input":"owoztneoer","output": "012"},
{"input":"fviefuro","output": "45"},
{"input":"zerozero","output": "00"},
{"input":"owoztneoer","output": "012"},
{"input":"fviefuro","output":"45"},
]
for t in test:
    r=s.originalDigits(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))


