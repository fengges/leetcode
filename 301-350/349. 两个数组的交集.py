class Solution:
    def intersection(self, nums1, nums2):
        dicA={}
        dicB={}
        for i in nums1:
            if i in dicA:
                dicA[i]+=1
            else:
                dicA[i]=1
        for i in nums2:
            if i in dicB:
                dicB[i]+=1
            else:
                dicB[i]=1
        r=[]
        for k in dicA:
            if k in dicB:
                r.append(k)
        return r