class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        if sum(nums) < target: return 0
        l, r = 0, 0
        curSum = 0
        res = float("inf")
        
        while r < len(nums):
            curSum += nums[r]
            while curSum >= target:
                res = min(res, r-l+1)
                curSum -= nums[l]
                l += 1
            
            r += 1
        
        return res
#         l, r = 0, len(nums) - 1
#         curSum = sum(nums)
#         minLen = float("inf")
        
#         while curSum >= target:
#             minLen = min(minLen, r-l+1)     
#             if nums[l] <= nums[r]:
#                 curSum -= nums[l]
#                 l += 1
#             else:
#                 curSum -= nums[r]
#                 r -= 1
        
#         return minLen
        
