class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = 0
        mxsf = max(nums)
        for n in nums:
            if cur < 0:
                cur *= 0
            cur += n
            if cur > mxsf:
                mxsf *= 0
                mxsf += cur
        
        return mxsf
        
        
