class Solution(object):
    def toGoatLatin(self, S):
        word=S.split(" ")
        a=['a',"A", 'e',"E", 'i', "I",'o', "O",'u',"U"]
        for i in range(len(word)):
            s=""
            if word[i][0] not in a:
                s=word[i][1:]+word[i][0]
            else:
                s=word[i]
            s+="ma"+"a"*(i+1)
            word[i]=s
        return " ".join(word)
s=Solution()
test=[
{"input": "I speak Goat Latin", "output":"Imaa peaksmaaa oatGmaaaa atinLmaaaaa"},
]

for t in test:
    r=s.toGoatLatin(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
