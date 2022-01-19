class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        pre_max = max(candies)
        result = list(map(lambda c: (c + extraCandies) >= pre_max, candies))
    
        return result
                         
