class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        len1 = len(nums1)
        len2 = len(nums2)
        size = len1 + len2
        if (size % 2 == 1):
            k=int(size/2+1)
            return self.findKth(nums1,nums2,k)
        else:
            k=int(size/2)
            return (self.findKth(nums1,nums2,k)+self.findKth(nums1,nums2,k+1))/2

    def findKth(self,nums1,nums2,k):
        if (len(nums1) > len(nums2)) :
            return self.findKth(nums2,nums1,k)
        if len(nums1)==0:
            return nums2[k-1]
        elif len(nums2)==0:
            return nums1[k-1]
        elif k==1:
            return min(nums1[0],nums2[0])
        pa = min(int(k / 2),len(nums1))
        pb = k - pa
        if nums1[pa - 1] < nums2[pb - 1]:
            return self.findKth(nums1[pa:],nums2, k - pa)
        elif nums1[pa - 1] >nums2[pb - 1]:
            return self.findKth(nums1,nums2[pb:], k - pb)
        else:
            return nums1[pa-1]




s=Solution()

test=[
{"input": ([1, 2], [3,4]), "output": 2.5},
{"input": ([1,2,2], [1,2,3]), "output": 2.0},
{"input": ([3,3,3,3],[3,3,3,3]), "output": 3.0},
{"input": ([], [1]), "output": 1},
{"input":([1, 3],[2]),"output":2.0},
      ]

for t in test:
    r=s.findMedianSortedArrays(t['input'][0],t['input'][1])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.findMedianSortedArrays(t['input'][0], t['input'][1])