class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        size=len(arr)
        for i in range(size):
            for j in range(i+1,size):
                if arr[i]/2==arr[j] or arr[j]/2==arr[i]:
                    return True
        else:
            return False