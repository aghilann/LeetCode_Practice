class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if len(nums) == 0: return - 1
        
        left, right = 0, len(nums) - 1
        
    
        while left <= right:
            pivot = (right + left) // 2
            
            if nums[pivot] == target:
                return pivot
            elif nums[pivot] > target:
                right = pivot - 1
                
            elif nums[pivot] < target:
                left = pivot + 1

        return -1
            
            
            
            
            
