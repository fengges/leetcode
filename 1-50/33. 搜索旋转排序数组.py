class Solution:

    def search(self, A, target):
        left, right = 0, len(A) - 1
        while left <= right:
            mid = (left + right) // 2
            if A[mid] == target:
                return mid
                # mid左端是排好序的
            if A[mid] > A[left]:
                # 因为前面第11行的判断已经说明A[mid] != target了，所以不再考虑A[mid] = target的情况
                if A[mid] > target and A[left] <= target:
                    right = mid - 1
                else:
                    left = mid + 1
            elif A[mid] == A[left]:
                left+=1
            else:
                if A[mid] < target and A[right] >= target:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
    def search2(self,A, target):
        n=len(A)
        if n == 0:
            return -1
        left,right= 0, n - 1
        while left <= right:
            mid = int((left + right) / 2)
            if A[mid] == target:
                return mid
            elif A[mid] < A[right]:
                if A[mid] < target and A[right] >= target:
                    left = mid + 1
                else :
                    right = mid - 1
            else:
                if A[left] <= target and A[mid] > target:
                    right = mid - 1
                else :
                    left = mid + 1

        return -1


print(Solution().search([1,3,1,1,1],3))
