class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        all_sum = sum(nums)
        left_sum = 0
        for i in range(len(nums)):
            right_sum = all_sum - left_sum - nums[i]
            if left_sum == right_sum:
                return i
            left_sum += nums[i]
        
        return -1
        
        total = sum(nums) # O(n)
    
