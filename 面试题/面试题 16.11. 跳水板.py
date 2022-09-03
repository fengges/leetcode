class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        if shorter==longer:
            return [shorter*k]
        return [longer*i+(k-i)*shorter for i in range(k+1)]
