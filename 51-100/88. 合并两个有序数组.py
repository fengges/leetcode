class Solution:
    def merge(self, nums1, m, nums2, n):
        for i in range(m-1,-1,-1):
            nums1[n+i]=nums1[i]
        t,s1,s2=0,0,0
        while s1<m and s2<n:
            if nums1[n+s1]>=nums2[s2]:
                nums1[t]=nums2[s2]
                t+=1
                s2+=1
            else:
                nums1[t]=nums1[s1+n]
                t+=1
                s1+=1

        for i in range(s1,m):
            nums1[t]=nums1[i+n]
            t+=1
        for i in range(s2,n):
            nums1[t]=nums2[i]
            t += 1
        return nums1

test=[
{"input": [[1,2,4,5,6,0],5,[3],1], "output": [1,2,3,4,5,6]},
{"input": [[1],1,[],0], "output": [1]},
{"input": [[1,2,3,0,0,0],3,[2,5,6],3], "output": [1,2,2,3,5,6]},
]
s=Solution()
for t in test:
    r=s.merge(t['input'][0],t['input'][1],t['input'][2],t['input'][3])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))
        r = s.merge(t['input'][0], t['input'][1], t['input'][2], t['input'][3])