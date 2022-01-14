class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sqrs = map(lambda n: n**2, nums)
        sqrs = sorted(list(sqrs))
        return sqrs
        
