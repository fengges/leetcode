class Solution:
    def fullJustify(self, words, maxWidth):
        list=[]
        temp=[]
        left=maxWidth+1
        for w in words:
            if len(w)+1>left:
                left=maxWidth+1
                list.append(temp)
                temp=[]
            temp.append(w)
            left-=(len(w)+1)
        if len(temp)!=0:
            list.append(temp)
        result=[]
        for temp in list:
            all=0
            if len(temp)!=1:
                for t in temp:
                    all+=len(t)
                blank=maxWidth-all
                gap=int(blank/(len(temp)))+1
                last=blank%gap
                bl="".join([" " for i in range(gap)])
                s=bl.join(temp[0:-1])
                s+="".join([" " for i in range(last)])+temp[-1]

            else:
                s=temp[0]+''.join([" " for i in range(maxWidth-len(temp[0]))])
            result.append(s)
        return result

s=Solution()
test=[
{"input": [["This", "is", "an", "example", "of", "text", "justification."],16], "output": [
   "This    is    an",
   "example  of text",
   "justification.  "
]},
{"input": [["What","must","be","acknowledgment","shall","be"],16], "output":[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]},
{"input": [["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"],20], "output":[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]},
]

for t in test:
    r=s.fullJustify(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.fullJustify(t['input'][0], t['input'][1])



