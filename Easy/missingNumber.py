class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        prev = -1
        print(nums)
        
        for n in nums:
            if prev + 1 != n:
                return prev + 1
            prev = n
        
        return prev + 1
        
