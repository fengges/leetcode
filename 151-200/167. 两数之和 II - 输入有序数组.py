class Solution:
    def twoSum(self, numbers, target):
        result=[]
        for i in range(len(numbers)-1):
            for j in range(i+1,len(numbers)):
                if numbers[i]+numbers[j]==target:
                    return [i+1,j+1]
                elif   numbers[i]+numbers[j]>target:
                    break
        return  result

