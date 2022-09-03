class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        arr1=nums[::2]
        arr2=nums[1::2]
        arr1.sort()
        arr2.sort(reverse=True)
 
        size=len(nums)
        for i in range(size):
            if i%2==0:
                nums[i]=arr1[i//2]
            else:
                nums[i]=arr2[i//2]
        return nums