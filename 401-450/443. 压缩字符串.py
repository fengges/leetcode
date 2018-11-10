class Solution:
    def compress(self, chars):
        char=None
        num=0
        level=0
        size=len(chars)
        for t in range(size):
            c=chars[level]
            if c==char:
                del chars[level]
                num+=1
            else:
                if num>1:
                    for i in str(num):
                        chars.insert(level,i)
                        level+=1
                char=c
                level+=1
                num=1
        if num > 1:
            for i in str(num):
                chars.insert(level, i)
                level += 1
        return len(chars)
s=Solution()
test=[
{"input": ["a","b","b","b","b","b","b","b","b","b","b","b","b","a",'a'], "output":["a","b","1","2",'a']},
{"input": ["a"], "output":["a"]},
{"input": ["a","a","b","b","c","c","c"], "output":["a","2","b","2","c","3"]},
]

for t in test:
    r=s.compress(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))