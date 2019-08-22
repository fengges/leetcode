class Solution:

    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        text = text.split()
        List = []
        for index, word in enumerate(text):
            if index > len(text) - 3:
                break
            if word == first and text[index + 1] == second:
                List.append(text[index + 2])
        return List

    def findOcurrences2(self, text: str, first: str, second: str):
        seq=first+" "+second
        start=0
        size=len(seq)
        text+=" "
        r=[]
        while True:
            index=text.find(seq,start)
            if index==-1:
                break
            start=index+size+1
            index=text.find(" ",start)
            if index!=-1:
                r.append(text[start:index])
        return r
s=Solution()
test=[
{"input": ["alice is a good girl she is a good student","a","good"], "output":["girl","student"] },
{"input": ["jkypmsxd jkypmsxd kcyxdfnoa jkypmsxd kcyxdfnoa jkypmsxd kcyxdfnoa kcyxdfnoa jkypmsxd kcyxdfnoa","kcyxdfnoa","jkypmsxd"], "output":["girl","student"] },

]
for t in test:
    r=s.findOcurrences(t['input'][0],t['input'][1],t['input'][2])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
