class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        ans=0
        for o in operations:
            if o=="++X" or o=='X++':
                ans+=1
            else:
                ans-=1
        return ans
