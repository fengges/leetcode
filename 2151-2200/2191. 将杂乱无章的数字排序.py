class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def transfer(x: int) -> int:
            return int("".join(str(mapping[int(digit)]) for digit in str(x)))

        num_pairs = [(transfer(num), num) for num in nums]
        num_pairs.sort(key=lambda pair: pair[0])

        ans = [num for (_, num) in num_pairs]
        return ans

