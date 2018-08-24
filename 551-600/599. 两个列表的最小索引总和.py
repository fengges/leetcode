class Solution:
    def findRestaurant(self, list1, list2):
        dicA={}
        dicB={}
        for i in list1:
            if i in dicA:
                dicA[i]+=1
            else:
                dicA[i]=1
        for i in list2:
            if i in dicB:
                dicB[i]+=1
            else:
                dicB[i]=1
        minIndex=10000
        r=[]
        for k in dicA:
            if k in dicB:
                if list1.index(k)+list2.index(k)<minIndex:
                    minIndex=list1.index(k)+list2.index(k)
                    r=[k]
                elif list1.index(k)+list2.index(k)==minIndex:
                    r.append(k)
        return r

s = Solution()
test = [
{"input": [["Shogun","Tapioca Express","Burger King","KFC"],["KFC","Burger King","Tapioca Express","Shogun"]], "output": [[1,2,3,4]]},


]

for t in test:
    r = s.findRestaurant(t['input'][0],t['input'][1])
    if r != t['output']:
        print("error:" + str(t) + " out:" + str(r))
