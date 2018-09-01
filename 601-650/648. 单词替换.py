class Solution:
    def replaceWords(self, dict, sentence):
        words=sentence.split(" ")
        for i,w in enumerate(words):
            t=self.find(w,dict)
            if t:
                words[i]=t
        return " ".join(words)

    def find(self,w,dict):
        for d in dict:
            if w.find(d)==0:
                return d
        return None
