class Solution:

    def search(self, A, target):
        left, right = 0, len(A) - 1
        while left <= right:
            mid = (left + right) // 2
            if A[mid] == target:
                return mid
                # mid左端是排好序的
            if A[mid] >= A[left]:
                # 因为前面第11行的判断已经说明A[mid] != target了，所以不再考虑A[mid] = target的情况
                if A[mid] > target and A[left] <= target:
                    right = mid - 1
                else:
                    left = mid + 1
                    # 下面的else等同于elif A[mid] <= A[right]
            else:
                if A[mid] < target and A[right] >= target:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
