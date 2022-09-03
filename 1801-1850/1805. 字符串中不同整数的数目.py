class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        ans=['']
        for w in word:
            if w.isdigit():
                ans[-1]+=w
            elif ans[-1]!='':
                ans.append('')
        if ans[-1]=='':
            ans.pop()

        print(ans)
        t=set()
        for a in ans:
            t.add(int(a))
        return len(t)