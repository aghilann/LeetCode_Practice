class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        
        if len(nums) <= 1:
            return 0
        
        highest = max(nums)
        
        for n in nums:
            if (highest / 2) < n and n != highest:
                return -1
        
        return nums.index(highest)
