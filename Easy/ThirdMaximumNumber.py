class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        x = sorted(list(set(nums)), reverse=True)
        
        if len(x) < 3:
            return x[0]
        else:
            return x[2]
            
