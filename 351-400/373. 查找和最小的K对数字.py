class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        size1,size2=len(nums1),len(nums2)
        ans=[]
        for i in range(size1):
            for j in range(size2):
                ans.append([i,j,nums1[i]+nums2[j]])
        ans.sort(key=lambda x:x[2])

        ans=ans[:k]
        ans=[a[0:2] for a in ans]
        return ans