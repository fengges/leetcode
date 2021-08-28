class Solution:
    def spellchecker(self, wordlist, queries):
        arr1=[a.lower() for a in wordlist]
        arr2=[a.replace('a','*').replace('e','*').replace('i','*').replace('o','*').replace('u','*') for a in arr1]
        arr1=arr1.reverse()
        arr2=arr2.reverse()
        size=len(wordlist)
        ans=[]
        for w in queries:
            a1=w.lower()
            a2=a1.replace('a','*').replace('e','*').replace('i','*').replace('o','*').replace('u','*')
            if w in wordlist:
                ans.append(w)
            elif a1 in arr1:
                index=arr1.index(a1)
                ans.append(wordlist[size-1-index])
            elif a2 in arr2:
                index=arr2.index(a1)
                ans.append(wordlist[size-1-index])
            else:
                ans.append('')
        return ans
