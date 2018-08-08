class Solution:
    def hIndex(self, citations):
        citations.sort(reverse=True)
        r=False
        i=0
        for i in range(len(citations)):
            if citations[i]>i:
                continue
            else:
                r=True
                break
        if not r:
            return len(citations)
        return i
