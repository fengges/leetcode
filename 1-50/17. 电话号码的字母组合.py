class Solution:
    def letterCombinations(self, digits):
        if len(digits)==0:
            return []
        dic={
            '2':['a','b','c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r','s'],
            '8':['t','u','v'],
            '9': ['w', 'x', 'y','z'],
             }
        list=[]
        li=dic[str(digits[0])]
        for l in li:
            r=self.letterCombinations(digits[1:])
            if len(r)==0:
                return li
            else:
                for t in r:
                    list.append(l+t)
        return list


s=Solution()

test=[
{"input": "23","output":["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]},
      ]

for t in test:
    r=s.letterCombinations(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.letterCombinations(t['input'])
