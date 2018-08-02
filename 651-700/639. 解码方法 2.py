class Solution:
    def numDecodings(self, s):
        if len(s) == 0 or s[0] == "0":
            return 0
        c1, c2 = 1, 1
        for i in range(1, len(s)):
            if s[i] == '0':
                c1 = 0
            if s[i - 1] == '1' or (s[i - 1] == '2' and s[i] <= '6'):
                c1 = c1 + c2
                c2 = c1 - c2
            elif s[i - 1] == '1' and s[i]=="*":
                c1 = c1 + c2
                c2 = c1 - c2
            else:
                c2 = c1

        return c1

s = Solution()
test = [
    {"input": "17", "output": 2},
    {"input": "230", "output": 0},
    {"input": "110", "output": 1},
    {"input": "100", "output": 0},
    {"input": "101", "output": 1},

    {"input": "10", "output": 1},
    {"input": "12", "output": 2},
    {"input": "226", "output": 3},
]

for t in test:
    r = s.numDecodings(t['input'])
    if r != t['output']:
        print("error:" + str(t) + " out:" + str(r))
        r = s.numDecodings(t['input'])